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
