#!/usr/bin/env python3
"""The Moon Finally Answers Back — entry program.

DRAFT -> REVISED: the draft line was

    "You wished on me for a thousand years and never once asked how I was doing."

Three real improvements in the revision below:

1. "a thousand years" became "Four billion years of wishes, howls,
   and 3 a.m. promises" — the revision names all three things the
   brief says the Moon answers (wishes, howls, late-night promises),
   so the line speaks as the Moon to everyone staring up at once
   instead of to one vague wisher.
2. "You wished on me" became a list of what the Moon endured — the
   Moon is now the one keeping score, which is the wry, old, tired
   voice the judge brief asks for, and the em-dash turn makes it a
   comeback instead of a complaint.
3. "how I was doing" became "how I am doing" — present tense, so the
   punch lands right now, in one read, before the line ends.

The final line is 108 characters, one line, no trailing newline.
The program writes it to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python 3 standard library only, deterministic.
"""

import os

ENTRY = "Four billion years of wishes, howls, and 3 a.m. promises \u2014 and not one of you has ever asked how I am doing."

assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
