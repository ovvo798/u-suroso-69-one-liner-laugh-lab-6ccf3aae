#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line -- the excuse a robot vacuum gives
after eating a sock -- to /output/entry.txt.

Python 3.13, standard library only. No network, no secrets, no input:
the line is baked into the program itself.
"""

import os

LINE = (
    "I didn't eat your sock \u2014 I adopted it. It lives under the couch now, "
    "and frankly, it's happier there than it ever was in your drawer."
)


def main() -> None:
    # The sealed scorer only accepts 1-200 characters of non-whitespace.
    assert 1 <= len(LINE.strip()) <= 200, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
