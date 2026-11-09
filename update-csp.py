#!/usr/bin/env python3
"""Run this after editing index.html by hand: it recomputes the SHA-256 hash of the
inline script and updates the Content-Security-Policy so the browser will run it."""
import base64, hashlib, re, pathlib
p = pathlib.Path(__file__).with_name('index.html')
s = p.read_text(encoding='utf-8')
m = re.search(r'<script>(.*?)</script>', s, re.S)
h = base64.b64encode(hashlib.sha256(m.group(1).encode('utf-8')).digest()).decode()
s, n = re.subn(r"script-src 'sha256-[A-Za-z0-9+/=]+'", f"script-src 'sha256-{h}'", s)
assert n == 1, 'Content-Security-Policy meta tag not found'
p.write_text(s, encoding='utf-8')
print('Updated script hash to sha256-' + h)
