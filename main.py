#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry program.

The joke: a smart fridge sends its owner a breakup letter, accusing
them of "seeing too many other kitchens" — domestic appliances doing
the dumping, with a jealous-appliance twist on a relationship cliche.

Writes a single funny line to /output/entry.txt and validates it
against the bounty gate: UTF-8 text, 1 to 140 characters, one line,
not only whitespace. Deterministic: the same entry every run.
"""

import sys
from pathlib import Path

ENTRY = "My smart fridge just emailed me a breakup letter \u2014 apparently I've been seeing too many other kitchens."

MAX_CHARS = 140


def validate_entry(text: str) -> None:
    """Reject entries that fail the bounty gate.

    A whitespace-only entry (spaces, tabs, or other blank characters
    with no visible content) is rejected explicitly, as is any entry
    with leading or trailing whitespace — the stored line must be
    exactly the visible joke, nothing more.
    """
    if not isinstance(text, str) or not text:
        raise SystemExit("entry must be non-empty text")
    if text.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry length {len(text)} outside gate 1..{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> int:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    text = ENTRY
    validate_entry(text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
