#!/usr/bin/env python3
"""Add favicon (SVG data URL, black QR on white) to all PlainQR pages."""
import re, os

os.chdir(r'C:\Users\MiniPC\Projects\plainqr')

FILES = ['index', 'menu', 'wifi', 'business-card', 'pdf', 'youtube',
         'instagram', 'contact', 'event', 'location', 'payment', 'template']

# Simple black QR glyph on white, brand color #171717. URL-encoded for data: URI.
SVG = ("%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
       "%3Crect width='64' height='64' fill='%23fff'/%3E"
       # three finder patterns (top-left, top-right, bottom-left)
       "%3Crect x='6' y='6' width='18' height='18' fill='none' stroke='%23171717' stroke-width='6'/%3E"
       "%3Crect x='10' y='10' width='10' height='10' fill='%23171717'/%3E"
       "%3Crect x='40' y='6' width='18' height='18' fill='none' stroke='%23171717' stroke-width='6'/%3E"
       "%3Crect x='44' y='10' width='10' height='10' fill='%23171717'/%3E"
       "%3Crect x='6' y='40' width='18' height='18' fill='none' stroke='%23171717' stroke-width='6'/%3E"
       "%3Crect x='10' y='44' width='10' height='10' fill='%23171717'/%3E"
       # data modules
       "%3Crect x='30' y='6' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='30' y='14' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='38' y='14' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='30' y='30' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='38' y='30' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='46' y='30' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='30' y='38' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='38' y='46' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='46' y='38' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='46' y='46' width='5' height='5' fill='%23171717'/%3E"
       "%3Crect x='54' y='30' width='4' height='4' fill='%23171717'/%3E"
       "%3Crect x='54' y='38' width='4' height='4' fill='%23171717'/%3E"
       "%3Crect x='54' y='46' width='4' height='4' fill='%23171717'/%3E"
       "%3Crect x='30' y='54' width='4' height='4' fill='%23171717'/%3E"
       "%3Crect x='38' y='54' width='4' height='4' fill='%23171717'/%3E"
       "%3Crect x='46' y='54' width='4' height='4' fill='%23171717'/%3E"
       "%3C/svg%3E")

FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,' + SVG + '">\n'

def add_favicon(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<link rel="icon"' in content:
        print(f'{path}: уже есть favicon, пропуск')
        return False
    # Insert after canonical line
    m = re.search(r'(<link rel="canonical"[^>]*>\s*\n)', content)
    if not m:
        print(f'{path}: canonical не найден, пропуск')
        return False
    content = content[:m.end()] + '    ' + FAVICON + content[m.end():]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{path}: favicon добавлен')
    return True

for slug in FILES:
    add_favicon(slug + '.html')
