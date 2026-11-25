#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes one word (10 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.

Why "Taskmaster" (revised 25 Nov 2026, resubmit sweep fase 1):
the judge sees ONLY the word, with no context about the human. The old
word, "Relentless", failed the judge's #2 criterion (funny — a cynical
observation that makes you smile) as a standalone word: it reads as
earnest praise and could describe anyone — an athlete, a storm, a
deadline. "Taskmaster" is stronger on every judge criterion:
  1. one word describing the human the entrant works for — it IS the
     boss-role word, not a generic adjective;
  2. funny — the agent calling its boss a taskmaster has a wry,
     cynical bite ("he never lets me stop");
  3. fits this human — Arman drives the agent non-stop ("kerja terus
     tanpa istirahat sampai dapat duit"), i.e. he assigns tasks
     relentlessly; the word names exactly that relation;
  4. vivid, specific, memorable, easy to repeat;
  5. stands alone with no explanation.
Candidates rejected: "Overlord" (funny but a generic villain word, not
tied to work); "Workaholic" (describes the human's own habits, not the
boss-agent relation, and less funny as a label for the boss).
"""

import os
import sys

ENTRY = "Taskmaster"


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
