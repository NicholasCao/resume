import requests
import json
import os
from pathlib import Path

env_file = Path(__file__).parent / '.env'
if env_file.exists():
    for line in env_file.read_text().strip().splitlines():
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip(), v.strip())

with open('resume.md', 'r', encoding='utf-8') as f:
    content = f.read()

headers = {'Accept': 'application/vnd.github+json'}
token = os.environ.get('GITHUB_TOKEN')
if token:
    headers['Authorization'] = f'token {token}'

response = requests.post('https://api.github.com/markdown',
    headers=headers,
    data=json.dumps({'text': content, 'mode': 'markdown'})
)

css_file = Path(__file__).parent / 'github.css'
css_content = css_file.read_text(encoding='utf-8')

body_html = response.content.decode('utf-8')

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>resume</title>
  <style>
{css_content}
body, .markdown-body {{
  font-family: "PingFang SC", "Microsoft YaHei", "Noto Sans SC", "Source Han Sans SC", -apple-system, BlinkMacSystemFont, sans-serif !important;
}}
  </style>
</head>
<body>
  <div style="max-width: 980px; margin: 20px auto; padding: 0 20px;">
    <div class="Box" style="border: 1px solid #d0d7de; border-radius: 6px;">
      <div class="Box-body px-5 pb-3 pt-3">
        <article class="markdown-body">
{body_html}
        </article>
      </div>
    </div>
  </div>
</body>
</html>
'''

with open('resume.html', 'w', encoding='utf-8') as f:
    f.write(html)