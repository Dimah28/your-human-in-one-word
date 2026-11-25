#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes one word (10 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

ENTRY = "Relentless"


def validate_entry(text: str) -> None:
    """Fail loudly if the word breaks the bounty gate (UTF-8 text of 1-30
    characters, not only whitespace, exactly one word) instead of
    submitting a bad entry."""
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry is {len(text)} characters, must be 1-30")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be exactly one word (no spaces)")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
