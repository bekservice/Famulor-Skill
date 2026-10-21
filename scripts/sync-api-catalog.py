#!/usr/bin/env python3
"""Project public OpenAPI operations and verified CLI/SDK mappings into the skill.

Inputs are explicit; this script never needs credentials or changes the application.
See PUBLISHING.md for the maintainer refresh workflow.
"""

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "skills/famulor-skill/references/api"
METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
SCHEMA_KEYS = {
    "$ref", "type", "format", "nullable", "required", "enum", "const",
    "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf",
    "minLength", "maxLength", "pattern", "minItems", "maxItems", "uniqueItems",
    "minProperties", "maxProperties", "readOnly", "writeOnly", "discriminator",
}
SCHEMA_CHILDREN = {"items", "additionalProperties", "not", "contains"}
SCHEMA_LISTS = {"allOf", "oneOf", "anyOf", "prefixItems"}


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def dereference(value, spec):
    seen = set()
    while isinstance(value, dict) and "$ref" in value:
        ref = value["$ref"]
        if not ref.startswith("#/") or ref in seen:
            raise ValueError(f"Unsupported reference: {ref}")
        seen.add(ref)
        value = spec
        for key in ref[2:].split("/"):
            value = value[key.replace("~1", "/").replace("~0", "~")]
    return value


def project_schema(value):
    """Keep request validation structure; exclude prose, examples and sample values.

    Public input names (including write-only secret inputs) remain contract fields.
    We publish no credential values, source data or response property snapshots.
    """
    if isinstance(value, bool):
        return value
    if not isinstance(value, dict):
        return {}
    result = {key: value[key] for key in sorted(SCHEMA_KEYS & value.keys())}
    if "properties" in value:
        result["properties"] = {
            key: project_schema(child) for key, child in sorted(value["properties"].items())
        }
    for key in sorted(SCHEMA_CHILDREN & value.keys()):
        result[key] = project_schema(value[key])
    for key in sorted(SCHEMA_LISTS & value.keys()):
        result[key] = [project_schema(child) for child in value[key]]
    return result


def references(value):
    if isinstance(value, dict):
        if "$ref" in value:
            yield value["$ref"]
        for child in value.values():
            yield from references(child)
    elif isinstance(value, list):
        for child in value:
            yield from references(child)


def extract_sdk_descriptors(source):
    match = re.search(r"export const operationDescriptors = (\{[\s\S]*?\}) as const;", source)
    if not match:
        raise ValueError("Cannot read generated SDK descriptors")
    return json.loads(match[1])


def verify_sdk_hash(source, spec_hash):
    match = re.search(r'export const contractHash = "([a-f0-9]{64})";', source)
    if not match or match[1] != spec_hash:
        raise ValueError("SDK descriptors are stale: generate them from the same OpenAPI input")


def build_catalog(spec, cli, sdk, date, spec_hash, docs=None):
    if cli.get("specSha256") != spec_hash:
        raise ValueError("CLI catalog is stale: regenerate it from the same OpenAPI input")
    cli_by_id = {item["operationId"]: item for item in cli["operations"]}
    operations = []
    ids = set()
    for path, raw_item in sorted(spec["paths"].items()):
        if not path.startswith("/") or path.startswith(("/api/", "/admin/", "/internal/")):
            raise ValueError(f"Not a public relative API path: {path}")
        item = dereference(raw_item, spec)
        for method in sorted(METHODS & item.keys()):
            op = dereference(item[method], spec)
            op_id = op["operationId"]
            if op_id in ids:
                raise ValueError(f"Duplicate operationId: {op_id}")
            ids.add(op_id)
            command = cli_by_id[op_id]
            descriptor = sdk[op_id]
            for other in (command, descriptor):
                if other["method"] != method.upper() or other["path"] != path:
                    raise ValueError(f"Transport mapping mismatch: {op_id}")
            params = {}
            for raw in item.get("parameters", []) + op.get("parameters", []):
                p = dereference(raw, spec)
                params[(p["in"], p["name"])] = {
                    "name": p["name"], "in": p["in"], "required": bool(p.get("required")),
                    "schema": project_schema(p.get("schema", {})),
                    **{key: p[key] for key in ("style", "explode") if key in p},
                }
            body = dereference(op.get("requestBody", {}), spec)
            request_body = {
                "required": bool(body.get("required")),
                "content": {mime: project_schema(content.get("schema", {}))
                            for mime, content in sorted(body.get("content", {}).items())},
            }
            responses = {}
            for code, raw in sorted(op.get("responses", {}).items()):
                response = dereference(raw, spec)
                responses[code] = sorted(response.get("content", {}).keys())
            # Preserve real flag names: global flag collisions and branded names
            # cannot safely be inferred with a generic kebab-case conversion.
            cli_params = [{k: p[k] for k in ("name", "in", "flag", "position", "required", "type", "enum", "nullable") if k in p}
                          for p in command.get("params", [])]
            cli_fields = [{k: p[k] for k in ("name", "flag", "required", "type", "enum", "nullable", "itemType") if k in p}
                          for p in command.get("body", {}).get("fields", [])]
            operations.append({
                "operationId": op_id, "method": method.upper(), "path": path,
                "group": op.get("tags", ["Other"])[0], "summary": op.get("summary", op_id),
                "documentation": (docs or {}).get((method.upper(), path), "https://docs.famulor.io/api-reference/introduction"),
                "cli": {"command": command["command"], "hidden": bool(command.get("hidden")),
                        "parameters": cli_params, "bodyFields": cli_fields},
                "sdkMethod": f"client.api.{op_id}", "parameters": list(params.values()),
                "requestBody": request_body, "responses": responses,
                "binaryResponse": bool(descriptor.get("binary")),
            })
    if ids != set(cli_by_id) or ids != set(sdk):
        raise ValueError("OpenAPI, CLI and SDK do not contain the same operation IDs")
    definitions = {}
    pending = list(references(operations))
    while pending:
        ref = pending.pop()
        if ref in definitions:
            continue
        if not ref.startswith("#/components/schemas/"):
            raise ValueError(f"Unexpected request schema reference: {ref}")
        value = project_schema(dereference({"$ref": ref}, spec))
        definitions[ref] = value
        pending.extend(references(value))
    return {
        "schemaVersion": 1, "reviewedAt": date,
        "source": "Famulor public OpenAPI, CLI command catalog and TypeScript SDK operation descriptors",
        "openapiSha256": spec_hash, "baseUrl": "https://app.famulor.io/api/v1",
        "notice": "Dated navigation and request-shape snapshot, not a runtime validator. Check the live public schema and installed client before execution. Descriptions, examples, default values and response properties are intentionally omitted.",
        "operations": sorted(operations, key=lambda op: op["operationId"]),
        "definitions": dict(sorted(definitions.items())),
    }


def render(catalog):
    groups = defaultdict(list)
    for operation in catalog["operations"]:
        groups[operation["group"]].append(operation)
    files = {"catalog.json": json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"}
    intro = ["# Public API operation index", "",
             f"Reviewed {catalog['reviewedAt']}: **{len(catalog['operations'])} operations across {len(groups)} areas**. Every operation is cross-checked against the generated CLI catalog and TypeScript SDK descriptors.", "",
             "Use this index to find the right endpoint. Open only the relevant area; use [API, CLI and SDK guidance](../api-and-sdk.md) for authentication, execution and verification. Public reseller operations remain subject to the authenticated workspace's entitlement and permissions.", "",
             "Inspect a request's parameters, body constraints, actual CLI flags and response media types without network access:", "", "```bash",
             "python3 skills/famulor-skill/scripts/find-operation.py createAssistant",
             "python3 skills/famulor-skill/scripts/find-operation.py --search whatsapp", "```", "",
             "When installed separately, run the script from your installed skill folder as `python3 scripts/find-operation.py ...`. The lookup includes only reachable request-schema definitions. It omits examples, default values and response properties; the live public OpenAPI and installed client's help remain authoritative.", "",
             "The full API uses `https://app.famulor.io/api/v1` plus the relative paths shown here. The SDK method is always `client.api.<operationId>`. MCP tool names and schemas are separate; use the [MCP toolset references](../toolsets/assistants.md) to discover them instead of translating API names.", "",
             "| Area | Operations | Reference |", "| --- | ---: | --- |"]
    for group, ops in sorted(groups.items()):
        filename = slug(group) + ".md"
        intro.append(f"| {cell(group)} | {len(ops)} | [{cell(group)}]({filename}) |")
        lines = [f"# {group} API operations", "", f"Reviewed {catalog['reviewedAt']}. {len(ops)} public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)", "",
                 "Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.", "",
                 "Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.", "",
                 "| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |", "| --- | --- | --- | --- |"]
        for op in ops:
            command = "Browser flow / raw API" if op["cli"]["hidden"] else f"`famulor {op['cli']['command']}`"
            lines.append(f"| `{op['operationId']}` | `{op['method']} {cell(op['path'])}` | {command} | [{cell(op['summary'])}]({op['documentation']}) |")
        files[filename] = "\n".join(lines) + "\n"
    files["index.md"] = "\n".join(intro) + "\n"
    return files


def documentation_slug(value):
    # Mintlify removes punctuation in operation summaries, e.g.
    # "conversation.ended" -> "conversationended" and "segment's" -> "segments".
    return re.sub(r"[\s-]+", "-", re.sub(r"[^\w\s-]", "", value.lower())).strip("-")


def navigation_links(navigation, spec):
    """Resolve only endpoints explicitly published in English navigation.

    Mintlify's generated pages use the first OpenAPI tag and operation summary;
    a navigation group label does not override the tag's URL segment. Respect
    inherited OpenAPI configuration, custom directories and x-mint.href.
    https://www.mintlify.com/docs/api-playground/openapi-setup
    """
    result = {}

    def visit(node, configuration=None):
        if isinstance(node, list):
            for child in node:
                visit(child, configuration)
        elif isinstance(node, dict):
            if node.get("language", "en") != "en":
                return
            configuration = node.get("openapi", configuration)
            for key in ("languages", "tabs", "groups", "pages", "anchors", "versions", "products"):
                if key in node:
                    visit(node[key], configuration)
        elif isinstance(node, str):
            match = re.fullmatch(r"(?:(\S+)\s+)?(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(/\S*)", node)
            if not match:
                return
            source = match[1] or (configuration.get("source") if isinstance(configuration, dict) else configuration)
            # This catalog describes one public schema, not legacy specs that
            # happen to contain an overlapping path.
            if source != "/api-reference/openapi.json":
                return
            method, path = match[2], match[3]
            operation = spec.get("paths", {}).get(path, {}).get(method.lower())
            if not operation or operation.get("x-hidden"):
                return
            override = operation.get("x-mint", {}).get("href")
            if override:
                if not override.startswith("/") or override.startswith("//"):
                    raise ValueError("Generated documentation href must be a local documentation path")
                href = override
            elif operation.get("summary") and operation.get("tags"):
                directory = configuration.get("directory", "api-reference") if isinstance(configuration, dict) else "api-reference"
                href = "/" + "/".join((directory.strip("/"), documentation_slug(operation["tags"][0]), documentation_slug(operation["summary"])))
            else:
                # Do not guess method/path title generation or untagged routes.
                return
            result[(method, path)] = "https://docs.famulor.io" + href

    visit(navigation.get("navigation", navigation))
    return result


def documentation_links(folder, navigation=None, spec=None, overrides=None):
    links = navigation_links(navigation, spec) if navigation is not None and spec is not None else {}
    if folder:
        for path in sorted(folder.rglob("*.mdx")):
            match = re.search(r'^openapi:\s*["\']?(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+([^\n"\']+)', path.read_text(), re.M)
            if match:
                relative = path.relative_to(folder).with_suffix("").as_posix()
                links[(match[1], match[2].strip())] = f"https://docs.famulor.io/api-reference/{relative}"
    for override in overrides or []:
        key = (override["method"], override["path"])
        if spec is not None and not spec.get("paths", {}).get(key[1], {}).get(key[0].lower()):
            raise ValueError(f"Documentation override names an absent operation: {key}")
        if not override["url"].startswith("https://docs.famulor.io/"):
            raise ValueError("Documentation overrides must use the public Famulor documentation host")
        links[key] = override["url"]
    return links


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--openapi", required=True, type=Path)
    parser.add_argument("--cli-catalog", required=True, type=Path)
    parser.add_argument("--sdk-descriptors", required=True, type=Path)
    parser.add_argument("--docs-dir", type=Path)
    parser.add_argument("--navigation", type=Path, help="Mintlify docs.json; resolves published generated endpoint pages")
    parser.add_argument("--link-overrides", type=Path, default=ROOT / "scripts/api-doc-links.json", help="reviewed published URL aliases for renamed documentation titles")
    parser.add_argument("--date", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = args.openapi.read_bytes()
    spec = json.loads(source)
    spec_hash = hashlib.sha256(source).hexdigest()
    sdk_source = args.sdk_descriptors.read_text()
    verify_sdk_hash(sdk_source, spec_hash)
    navigation = json.loads(args.navigation.read_text()) if args.navigation else None
    overrides = json.loads(args.link_overrides.read_text())
    catalog = build_catalog(spec, json.loads(args.cli_catalog.read_text()),
                            extract_sdk_descriptors(sdk_source), args.date,
                            spec_hash, documentation_links(args.docs_dir, navigation, spec, overrides))
    files = render(catalog)
    stale = [name for name, text in files.items() if not (OUTPUT / name).exists() or (OUTPUT / name).read_text() != text]
    extra = [p.name for p in OUTPUT.glob("*.md") if p.name not in files]
    if extra:
        raise SystemExit("Obsolete generated references need review: " + ", ".join(extra))
    if args.check and stale:
        raise SystemExit("Stale API catalog: " + ", ".join(stale))
    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for name, text in files.items():
            temporary = OUTPUT / (name + ".tmp")
            temporary.write_text(text)
            temporary.replace(OUTPUT / name)
    deep_links = sum(not op["documentation"].endswith("/introduction") for op in catalog["operations"])
    print(f"{len(catalog['operations'])} public operations; {len(files)-2} areas; {deep_links} deep links; request contracts and CLI/SDK mappings verified")


if __name__ == "__main__":
    main()
