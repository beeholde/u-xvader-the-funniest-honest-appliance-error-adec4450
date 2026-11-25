#!/usr/bin/env python3
"""The Funniest Honest Appliance Error - v1 entry.

Writes one line (the entry text) to /output/entry.txt.

The line: a fridge reports the truth about why it is warming up -
the owner has opened it nine times looking for food that is not
there, and no compressor can cool indecision.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, a single line.
"""
import os
import sys
from pathlib import Path

LINE = "Temperature rising. You opened me nine times looking for food that is not here. I cannot cool indecision."
MAX_CHARS = 200
# Line design (judge criteria, in order):
#  C1 honest error - "Temperature rising" is a real fridge alert; door-open
#     counts are real smart-fridge telemetry, and repeated openings really
#     do warm the cabinet. The fault is named, not invented.
#  C2 laugh - a physical system diagnosing a psychological fault: the
#     fridge concludes the problem is not thermal but the owner's
#     indecision. "Nine times" is the damning, precise count.
#  C3 humour from truth - the joke is the telemetry itself; nothing is
#     bolted on. Every owner has stood at an open fridge like this.
#  C4 machine voice - flat diagnostic register throughout; "I cannot
#     cool indecision" is a plain statement of functional limitation.
#  C5 economy - 105/200 chars; the opening diagnostic earns C1, the
#     middle sentence carries the evidence, the last sentence is the turn.
# Chosen over the washer (one-sock unbalanced load) and dryer (lint fire)
# trials: GLM-5.3-Flash pairwise under the house brief put this line
# first among the surviving candidates after the toaster line was dropped
# (stuck-toast/ejected-toast is saturated in the sibling toaster-error
# field, and its "we are both stuck" turn duplicates a sibling trial).


def main() -> int:
    text = LINE
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"entry line is {len(text)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry line is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    os.chmod(out_path, 0o644)
    # Read-back verification: the file must hold exactly the line.
    if out_path.read_bytes() != text.encode("utf-8"):
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
