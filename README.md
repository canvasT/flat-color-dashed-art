# Flat Color & Dashed Art

A Codex Skill that turns an uploaded image into three matched assets:

1. a layout-preserving flat-color 2D illustration;
2. a dashed-outline tracing/coloring sheet generated from that flat-color master;
3. a programmatically composed worksheet with a large dashed drawing and a small color reference at the upper right.

The workflow preserves the uploaded image's own composition. It does not force A4 or a four-panel layout.

## Install

Clone the repository directly into your Codex skills directory:

```bash
git clone https://github.com/YOUR_ACCOUNT/flat-color-dashed-art.git ~/.agents/skills/flat-color-dashed-art
```

Restart or reload Codex after installation.

## Use

Upload an image and ask:

```text
Use $flat-color-dashed-art to create the flat-color version, matching dashed outline, and final tracing worksheet for this image.
```

By default, the Skill generates and checks the two master images, then uses a deterministic Pillow script for the final worksheet layout. Existing files are never overwritten.

## Repository contents

- `SKILL.md` — routing and workflow instructions
- `references/prompts.md` — reusable generation and correction prompts
- `assets/flat-color-style-reference.png` — bundled flat-color style reference
- `assets/dashed-outline-style-reference.png` — bundled dashed-line style reference
- `assets/worksheet-layout-reference.png` — bundled layout reference
- `scripts/compose_worksheet.py` — deterministic final-page compositor
- `agents/openai.yaml` — Codex UI metadata

Requires a Codex environment with the built-in image generation tool and Python with Pillow.
