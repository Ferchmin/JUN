#!/usr/bin/env python3
"""Check that every relative Markdown link in the repository resolves to a real path.

Run from the repository root:

    python3 scripts/check_links.py

Only relative links are checked; external URLs and in-page anchors are skipped. The
repository README linked a `examples/counter/` directory that did not exist for two
releases, which is the class of error this catches.
"""

import os
import re
import sys

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def markdown_files() -> list[str]:
    found = []
    for root, dirnames, filenames in os.walk("."):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for filename in filenames:
            if filename.endswith(".md"):
                found.append(os.path.join(root, filename))
    return sorted(found)


def main() -> int:
    broken = []
    checked = 0

    for path in markdown_files():
        with open(path, encoding="utf-8") as handle:
            text = handle.read()

        for target in LINK.findall(text):
            target = target.split(" ", 1)[0].strip()
            if not target or target.startswith(SKIP_PREFIXES):
                continue

            resolved = os.path.normpath(
                os.path.join(os.path.dirname(path), target.split("#", 1)[0])
            )
            checked += 1
            if not os.path.exists(resolved):
                broken.append((path, target))

    for path, target in broken:
        print(f"FAIL {path}: {target} does not exist")

    print(f"checked {checked} relative link(s), {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
