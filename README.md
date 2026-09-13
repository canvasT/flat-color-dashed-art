# Flat Color & Dashed Art

A Codex Skill that turns an uploaded image into a matched pair:

1. a layout-preserving flat-color 2D illustration;
2. a dashed-outline tracing/coloring sheet generated from that flat-color master.

The workflow preserves the uploaded image's own composition. It does not force A4 or a four-panel layout.

## Install

Clone the repository directly into your Codex skills directory:

```bash
git clone https://github.com/YOUR_ACCOUNT/flat-color-dashed-art.git ~/.codex/skills/flat-color-dashed-art
```

Restart or reload Codex after installation.

## Use

Upload an image and ask:

```text
Use $flat-color-dashed-art to create the flat-color version and matching dashed-outline version of this image.
```

By default, the Skill completes both stages, visually checks each output, retries targeted style corrections when necessary, and saves both images without overwriting existing files.

## Repository contents

- `SKILL.md` — routing and workflow instructions
- `references/prompts.md` — reusable generation and correction prompts
- `assets/flat-color-style-reference.png` — bundled flat-color style reference
- `assets/dashed-outline-style-reference.png` — bundled dashed-line style reference
- `agents/openai.yaml` — Codex UI metadata

Requires a Codex environment with the built-in image generation tool.

