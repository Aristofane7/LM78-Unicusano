#!/usr/bin/env python3
"""Conta le battute (spazi inclusi) della relazione seminari, esclusi commenti HTML e frontmatter."""
import re
import sys
from pathlib import Path

SOGLIA = 10_000
path = Path(sys.argv[1])
txt = path.read_text(encoding="utf-8")
txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)
txt = re.sub(r"\A---\n.*?\n---\n", "", txt, flags=re.S)
corpo = re.sub(r"\n{2,}", "\n", txt).strip()
n = len(corpo.replace("\n", " "))
print(f"{path}: {n} battute (spazi inclusi), soglia {SOGLIA}: {'OK' if n >= SOGLIA else f'mancano {SOGLIA - n}'}")
sys.exit(0 if n >= SOGLIA else 1)
