# Loading-screen tip entry (Python 3.13, standard library only).
# Writes one fixed tip to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One line, 115 characters: a loading-screen tip for stressed developers
# and AI coding agents. The agent rewrites the dev's 2 a.m. function and
# confesses, in a code comment, that it has no idea what it does either --
# both sides of the keyboard feel seen by the same punchline.
TIP = "Tip: Your agent just rewrote the function you wrote at 2 a.m. It left one comment: 'No idea what this does either.'"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(TIP, encoding="utf-8")
