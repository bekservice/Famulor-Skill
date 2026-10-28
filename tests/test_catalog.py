"""Offline contract coverage and public projection regression checks."""
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/famulor-skill"


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


sync = module(ROOT / "scripts/sync-api-catalog.py", "sync_api_catalog")
lookup = module(SKILL / "scripts/find-operation.py", "find_operation")


class PublicCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((SKILL / "references/api/catalog.json").read_text())

    def test_unique_complete_release_catalog(self):
        operations = self.catalog["operations"]
        self.assertEqual(len(operations), 501)
        self.assertEqual(len({op["operationId"] for op in operations}), 501)
        self.assertEqual(len({(op["method"], op["path"]) for op in operations}), 501)
        self.assertEqual(len({op["group"] for op in operations}), 40)
        self.assertEqual(sum(op["cli"]["hidden"] for op in operations), 4)
        for op in operations:
            self.assertEqual(op["sdkMethod"], "client.api." + op["operationId"])
            self.assertFalse(op["path"].startswith(("/api/", "/admin/", "/internal/")))

    def test_all_references_resolve_and_detail_is_scoped(self):
        for op in self.catalog["operations"]:
            detail = lookup.operation_contract(self.catalog, op)
            for ref in lookup.schema_references(detail["operation"]):
                self.assertIn(ref, detail["definitions"])
            for definition in detail["definitions"].values():
                for ref in lookup.schema_references(definition):
                    self.assertIn(ref, detail["definitions"])
        plain = next(op for op in self.catalog["operations"] if op["operationId"] == "getMe")
        self.assertEqual(lookup.operation_contract(self.catalog, plain)["definitions"], {})

    def test_generated_markdown_matches_json(self):
        for name, content in sync.render(self.catalog).items():
            self.assertEqual((SKILL / "references/api" / name).read_text(), content, name)

    def test_schema_projection_keeps_constraints_not_sample_values(self):
        source = {"type": "object", "description": "private implementation prose", "example": {"token": "secret"},
                  "required": ["mode"], "properties": {
                      "mode": {"type": "string", "enum": ["a", "b"], "default": "a"},
                      "token": {"type": "string", "writeOnly": True, "example": "secret"},
                      "choices": {"type": "array", "minItems": 1, "items": {"oneOf": [{"type": "string"}, {"type": "integer"}]}}}}
        result = sync.project_schema(source)
        self.assertEqual(result["required"], ["mode"])
        self.assertEqual(result["properties"]["mode"]["enum"], ["a", "b"])
        self.assertTrue(result["properties"]["token"]["writeOnly"])
        self.assertNotIn("secret", json.dumps(result))
        self.assertNotIn("default", result["properties"]["mode"])
        self.assertEqual(result["properties"]["choices"]["minItems"], 1)

    def test_projection_has_no_examples_descriptions_or_response_properties(self):
        def visit(value):
            if isinstance(value, dict):
                self.assertFalse({"example", "examples", "default", "description"} & value.keys())
                for key, child in value.items():
                    if key == "properties":
                        for schema in child.values():
                            visit(schema)
                    else:
                        visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)
        for op in self.catalog["operations"]:
            visit(op["requestBody"])
            for content_types in op["responses"].values():
                self.assertTrue(isinstance(content_types, list))
                self.assertTrue(all(isinstance(item, str) for item in content_types))
        for definition in self.catalog["definitions"].values():
            visit(definition)
        # Property names can legitimately be 'description' or 'default'; inspect
        # schema nodes rather than banning those strings from public contracts.

    def test_offline_lookup_exact_command_and_search(self):
        result = subprocess.run([sys.executable, str(SKILL / "scripts/find-operation.py"), "list-assistants"],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout)["operation"]["operationId"], "listAssistants")
        matches = lookup.search(self.catalog, "whatsapp")
        self.assertTrue(any(op["operationId"] == "listWhatsAppTemplates" for op in matches))
        self.assertEqual(lookup.search(self.catalog, "nonexistent-unique-operation"), [])

    def test_regenerator_rejects_stale_client_contract(self):
        with self.assertRaisesRegex(ValueError, "CLI catalog is stale"):
            sync.build_catalog({}, {"specSha256": "old"}, {}, "2026-10-21", "new")
        with self.assertRaisesRegex(ValueError, "SDK descriptors are stale"):
            sync.verify_sdk_hash('export const contractHash = "' + 'a' * 64 + '";', 'b' * 64)

    def test_navigation_links_follow_published_schema_tags_and_overrides(self):
        spec = {"paths": {
            "/things": {"get": {"summary": "List a segment's things", "tags": ["Actual tag"]}},
            "/test": {"post": {"summary": "Send conversation.ended", "tags": ["Things"]}},
            "/custom": {"get": {"summary": "Custom", "tags": ["Things"], "x-mint": {"href": "/guide/custom"}}},
            "/not-published": {"get": {"summary": "Not published", "tags": ["Things"]}},
            "/hidden": {"get": {"summary": "Hidden", "tags": ["Things"], "x-hidden": True}},
            "/legacy": {"get": {"summary": "Legacy", "tags": ["Things"]}},
        }}
        navigation = {"navigation": {"languages": [
            {"language": "en", "groups": [{"group": "Different label", "openapi": "/api-reference/openapi.json",
              "pages": ["GET /things", "POST /test", "GET /custom", "GET /hidden",
                        {"group": "Legacy", "openapi": "/legacy.json", "pages": ["GET /legacy"]}]}]},
            {"language": "de", "openapi": "/api-reference/openapi.json", "pages": ["GET /not-published"]},
        ]}}
        links = sync.navigation_links(navigation, spec)
        self.assertEqual(links[("GET", "/things")], "https://docs.famulor.io/api-reference/actual-tag/list-a-segments-things")
        self.assertEqual(links[("POST", "/test")], "https://docs.famulor.io/api-reference/things/send-conversationended")
        self.assertEqual(links[("GET", "/custom")], "https://docs.famulor.io/guide/custom")
        self.assertEqual(len(links), 3)

    def test_reviewed_url_alias_does_not_guess_a_renamed_slug(self):
        spec = {"paths": {"/things": {"get": {"summary": "Renamed", "tags": ["Things"]}}}}
        override = [{"method": "GET", "path": "/things", "url": "https://docs.famulor.io/api-reference/things/original-title"}]
        links = sync.documentation_links(None, spec=spec, overrides=override)
        self.assertEqual(links[("GET", "/things")], override[0]["url"])
        with self.assertRaisesRegex(ValueError, "absent operation"):
            sync.documentation_links(None, spec={"paths": {}}, overrides=override)


if __name__ == "__main__":
    unittest.main()
