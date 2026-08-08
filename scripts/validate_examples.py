#!/usr/bin/env python3
"""Validate the JUN schema, then validate every example document against it.

Run from the repository root:

    pip install jsonschema && python3 scripts/validate_examples.py

Exits non-zero if the schema is not valid draft-07, if any example fails validation,
or if no examples were found (which would otherwise let the check pass vacuously).
"""

import glob
import json
import sys

from jsonschema import Draft7Validator

SCHEMA_PATH = "schemas/jun.schema.json"
EXAMPLE_GLOB = "examples/*/screen.json"


def main() -> int:
    with open(SCHEMA_PATH) as handle:
        schema = json.load(handle)

    Draft7Validator.check_schema(schema)
    print(f"{SCHEMA_PATH}: valid JSON Schema draft-07")

    validator = Draft7Validator(schema)
    paths = sorted(glob.glob(EXAMPLE_GLOB))

    if not paths:
        print(f"error: no examples matched {EXAMPLE_GLOB}", file=sys.stderr)
        return 1

    failed = False
    for path in paths:
        try:
            with open(path) as handle:
                document = json.load(handle)
        except json.JSONDecodeError as error:
            print(f"FAIL {path}: not valid JSON: {error}")
            failed = True
            continue

        errors = sorted(validator.iter_errors(document), key=lambda e: list(e.path))
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                location = "/".join(str(part) for part in error.path) or "<root>"
                print(f"       {location}: {error.message}")
        else:
            print(f"OK   {path}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
