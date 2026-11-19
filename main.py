#!/usr/bin/env python3
"""News-image entry: copy the composed digest to /output/entry.png.

The image (entry.png beside this file) sums up the world news of Wednesday
18 November 2026. It runs twice in the grader; both runs write identical
bytes. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(src, dst)
# Both grader runs must write the same bytes: fail loudly instead of
# silently shipping a partial copy.
assert os.path.getsize(src) == os.path.getsize(dst), "copy size mismatch"
