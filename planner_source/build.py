# -*- coding: utf-8 -*-
"""
Planner TDAH Produtivo - CATreport
Build script: assembles all page sections into index.html
"""
import os
import importlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages import intro, methods, goals, monthly, weekly, daily
from pages import trackers, finance, health, study, reflection, notes

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

HEAD = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Planner TDAH Produtivo - CATreport</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
'''

TAIL = '''
</body>
</html>'''

sections = [
    intro,
    methods,
    goals,
    monthly,
    weekly,
    daily,
    trackers,
    finance,
    health,
    study,
    reflection,
    notes,
]

all_pages = []
for section in sections:
    all_pages.extend(section.get_pages())

html = HEAD
for page in all_pages:
    html += page + "\n\n"
html += TAIL

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Gerado: {OUTPUT}")
print(f"Total de paginas: {len(all_pages)}")
