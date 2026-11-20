# A working news-image entry (Python 3.13, standard library only): its image is
# the entry.png beside this file, and the program copies it to /output/entry.png.
# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels,
# and the judge sees exactly the bytes copied. No network, fully deterministic:
# every run writes the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
