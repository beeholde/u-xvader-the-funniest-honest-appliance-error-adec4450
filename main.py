#!/usr/bin/env python3
"""The Funniest Honest Appliance Error - v2 entry.

Writes one line (the entry text) to /output/entry.txt.

The line: a washer aborts its spin because the load is unbalanced -
the owner put in a single shoe, and the honest fix is the other shoe.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, a single line.
"""
import os
import sys
from pathlib import Path

LINE = "Spin aborted: unbalanced load. One shoe detected. Add the other shoe."
MAX_CHARS = 200
# Line design (judge criteria, in order):
#  C1 honest error - "Spin aborted: unbalanced load" is a real washer
#     fault report; a single shoe really does unbalance a spin cycle.
#     The fault is named, not invented.
#  C2 laugh - the fix is the joke: the machine's honest remedy for one
#     shoe is the other shoe, stated as a plain instruction.
#  C3 humour from truth - nothing is bolted on; the absurdity is the
#     owner's load choice, reported without comment.
#  C4 machine voice - flat diagnostic register throughout; no punchline
#     announces itself, the line reads like a status readout.
#  C5 economy - 69/200 chars; fault, cause, and fix in three short
#     beats, every word load-bearing.
# Rebuild context: v1 (fridge "cannot cool indecision") graded R1
# 0.447544, rank 1335/1899 - outside the final-heat top 500. This line
# evolves the v1 backup (one-sock unbalanced load) away from the sock
# angle, which the R1 board already holds ("Error 04: The Missing
# Sock" ranked directly above v1), and drops v1's crafted-punchline
# structure for a purely functional instruction.


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
