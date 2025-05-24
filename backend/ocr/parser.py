# backend/ocr/parser.py

import re

def clean_text(text):
    lines = text.split("\n")
    items = [line.strip() for line in lines if re.search(r'\d', line)]
    return items
