#!/usr/bin/env python3
"""One Line, One Laugh.

Writes a single funny line, a joke about anything at all, capped at
140 characters, to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 140

LINE = "I asked the barista for something strong. She slid me her two weeks' notice."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-140 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
