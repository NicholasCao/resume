#!/bin/bash
# 使用 Playwright (Chromium) 将 resume.html 渲染为 PDF

DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT="$DIR/resume.html"
OUTPUT="$DIR/resume.pdf"

python3 << 'EOF'
from playwright.sync_api import sync_playwright
import sys, os

dir_path = os.environ.get('DIR', os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(dir_path, 'resume.html')
output_path = os.path.join(dir_path, 'resume.pdf')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f'file://{input_path}', wait_until='networkidle')
    page.pdf(path=output_path, format='A4', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
    browser.close()
EOF

echo "PDF generated: $OUTPUT"
