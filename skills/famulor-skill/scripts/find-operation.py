#!/usr/bin/env python3
"""Find a Famulor public endpoint and its reviewed request contract offline.

No credentials, network calls or mutations. Example: find-operation.py createAssistant
"""

import argparse
import json
from pathlib import Path


def schema_references(value):
    if isinstance(value, dict):
        if "$ref" in value:
            yield value["$ref"]
        for child in value.values():
            yield from schema_references(child)
    elif isinstance(value, list):
        for child in value:
            yield from schema_references(child)


def operation_contract(catalog, operation):
    definitions = {}
    pending = list(schema_references(operation))
    while pending:
        ref = pending.pop()
        if ref in definitions:
            continue
        definitions[ref] = catalog["definitions"][ref]
        pending.extend(schema_references(definitions[ref]))
    return {"reviewedAt": catalog["reviewedAt"], "baseUrl": catalog["baseUrl"],
            "notice": catalog["notice"], "operation": operation,
            "definitions": dict(sorted(definitions.items()))}


def search(catalog, query):
    terms = query.lower().split()
    return [op for op in catalog["operations"] if all(term in " ".join(
        [op["operationId"], op["cli"]["command"], op["path"], op["group"], op["summary"]]
    ).lower() for term in terms)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="operation ID or CLI command for full request details")
    parser.add_argument("--search", dest="search_query", help="search operation names, paths and summaries")
    parser.add_argument("--groups", action="store_true", help="list API areas")
    args = parser.parse_args()
    catalog = json.loads((Path(__file__).resolve().parent.parent / "references/api/catalog.json").read_text())
    if args.groups:
        result = [{"group": group, "operations": sum(op["group"] == group for op in catalog["operations"])}
                  for group in sorted({op["group"] for op in catalog["operations"]})]
    elif args.search_query is not None:
        result = [{key: op[key] for key in ("operationId", "method", "path", "group", "summary", "sdkMethod")}
                  | {"cliCommand": None if op["cli"]["hidden"] else f"famulor {op['cli']['command']}"}
                  for op in search(catalog, args.search_query)]
    elif args.query:
        matches = [op for op in catalog["operations"] if args.query in (op["operationId"], op["cli"]["command"])]
        if not matches:
            parser.error("No exact operation. Use --search to discover a name.")
        result = operation_contract(catalog, matches[0])
    else:
        parser.error("Provide an operation ID, --search TEXT, or --groups.")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
