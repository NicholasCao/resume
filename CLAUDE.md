# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

个人简历项目，维护中英文简历内容，支持 Markdown 编写并通过 GitHub Markdown API 渲染为 HTML，最终导出 PDF。

## Key Files

- `resume.md` — 最新简历正文（Markdown），这是当前使用的主简历
- `generate.py` — 调用 GitHub Markdown API 将 `resume.md` 渲染为 `resume.html`
- `github.css` — GitHub 风格样式表，HTML 简历引用此文件
- `resume.html` — 渲染后的 HTML 简历（由 generate.py 生成）
- `legacy/` — 历史版本，按年份命名（2019-resume.md、2025-resume.md 等）

## Commands

生成 HTML 简历：

```bash
python generate.py
```

该脚本读取 `resume.md`，通过 `https://api.github.com/markdown` 渲染后写入 `resume.html`。需要 `requests` 库。

## Workflow

1. 编辑 `resume.md` 更新简历内容
2. 运行 `python generate.py` 生成 HTML
3. 在浏览器中打开 `resume.html` 预览，打印/导出为 PDF

## Notes

- 简历语言为中文，编辑时保持中文
