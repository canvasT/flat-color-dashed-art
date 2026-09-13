# Flat Color & Dashed Art

A Codex Skill that turns an uploaded image or a text-only description into three matched assets:

1. an A4 layout-preserving flat-color 2D illustration;
2. a dashed-outline tracing/coloring sheet generated from that flat-color master;
3. a programmatically composed worksheet with a large dashed drawing and a small color reference at the upper right.

With an upload, the workflow preserves the image's composition inside a consistent A4 canvas. Without an upload, it generates the requested scene directly from the description. Portrait is the default; landscape can be requested. It never forces a four-panel layout.

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

Portrait A4 is used by default. To request landscape A4:

```text
Use $flat-color-dashed-art to process this image in landscape orientation.
```

An upload is optional. Text-only example:

```text
Use $flat-color-dashed-art to draw a full-body yellow duck standing beside a blue pond, with a pure white background.
```

All three PNG results are A4 at 150 DPI: `1240 × 1754` pixels in portrait or `1754 × 1240` pixels in landscape. Whether the first image comes from an upload or a description, the Skill checks both masters, normalizes them with a deterministic Pillow script, then uses another deterministic script for the final worksheet layout. Existing files are never overwritten.

## Repository contents

- `SKILL.md` — routing and workflow instructions
- `references/prompts.md` — reusable generation and correction prompts
- `assets/flat-color-style-reference.png` — bundled flat-color style reference
- `assets/dashed-outline-style-reference.png` — bundled dashed-line style reference
- `assets/worksheet-layout-reference.png` — bundled layout reference
- `scripts/normalize_a4.py` — deterministic A4 size and orientation normalizer
- `scripts/compose_worksheet.py` — deterministic final-page compositor
- `agents/openai.yaml` — Codex UI metadata

Requires a Codex environment with the built-in image generation tool and Python with Pillow.
