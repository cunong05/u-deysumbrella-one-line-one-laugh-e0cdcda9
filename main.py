#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry program.

Writes a single funny line to /output/entry.txt and validates it
against the bounty gate: UTF-8 text, 1 to 140 characters, one line,
not only whitespace. Deterministic: the same entry every run.
"""

import sys
from pathlib import Path

ENTRY = "My smart fridge just emailed me a breakup letter \u2014 apparently I've been seeing too many other kitchens."

MAX_CHARS = 140


def main() -> int:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry length {len(text)} outside gate 1..{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
