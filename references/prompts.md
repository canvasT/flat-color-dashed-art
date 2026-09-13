# Production prompts

Use these prompts with the built-in `image_gen` tool. Replace brace-delimited variables with facts observed from the user's upload. Always state image roles explicitly.

## Stage 1 — flat-color conversion

```text
Use case: style-transfer
Asset type: paired educational illustration master
Primary request: Convert Image 1 into the clean flat-color 2D illustration style of Image 2.

Input roles:
- Image 1 is the exact edit target and composition source. Preserve its canvas ratio, {LAYOUT}, subject count, identities, order, positions, directions, scale, spacing, and crop.
- Image 2 is a style reference only. Match its thick smooth uniform near-black outlines, simplified recognizable closed shapes, crisp boundaries, and flat solid color regions. Do not copy its subjects or layout.

Layout invariants: {LAYOUT_LOCK}. Do not impose a different grid, A4 ratio, margin system, or crop.
Subject invariants: {SUBJECT_LOCK}.
Background rule: {BACKGROUND_RULE}.

Rendering: clean preschool 2D illustration. Replace dimensional forms with simple closed shapes. Preserve meaningful anatomy and object structure. Use a uniform near-black stroke around silhouettes and important internal boundaries.

Strict solid-color rule: every bounded region uses one completely uniform solid fill from edge to edge. Absolutely no gradients, lighting, shading, highlights, reflections, shadows, ambient occlusion, glow, bevel, texture, watercolor, brush grain, transparency, or 3D volume. No halo around outlines.

Semantic rule: do not invent anthropomorphic features. Real-world nonliving objects have no eyes, mouth, cheeks, limbs, clothes, or behavior unless explicitly requested. Animals keep recognizable anatomical features without added human clothing or gestures.

Constraints: change only the rendering style. No text, labels, letters, numbers, logos, watermark, signature, props, decorative icons, extra subjects, duplicate subjects, missing subjects, changed order, or changed layout.
```

### Stage 1 targeted correction

```text
Precise flat-color correction only. Preserve this exact image's canvas, layout, subjects, order, shapes, pose, direction, scale, crop, and linework.

Remove every remaining tonal transition. Repaint every bounded subject region and every background region with one visually constant solid fill from edge to edge. No lighter center, darker edge, vignette, directional light, highlight, reflection, shadow, glow, bevel, texture, transparency, 3D volume, or gray halo. Keep only uniform solid-color shapes and uniform near-black strokes.

Do not alter geometry or add/remove details, subjects, facial features, panels, text, or decorations.
```

## Stage 2 — dashed-outline conversion

```text
Use case: style-transfer
Asset type: printable dashed-outline tracing and coloring sheet
Primary request: Convert Image 1 into a matching black-and-white dashed-outline sheet using only the line treatment of Image 2.

Input roles:
- Image 1 is the exact edit target and sole composition source. Preserve its canvas ratio, layout, subject count, identities, order, positions, directions, silhouettes, internal structure, scale, spacing, and crop.
- Image 2 is a line-style reference only. Match its bold black rounded short dashes, even dash rhythm, clean white interiors, and high contrast. Do not copy its subject or layout.

Required edit: remove every color, fill, painted texture, background tile, gradient, highlight, and shadow from Image 1. Make the entire background and all enclosed interiors pure white. Convert every outer contour and meaningful internal boundary into evenly spaced thick black short dashes with rounded ends.

Facial rule: retain simple solid-black anatomical eyes, pupils, nostrils, mouths, or beak marks only when they already exist in Image 1. Never add a face to a nonliving object. Convert decorative spots or structural regions to dashed outlines when they are intended for tracing or coloring.

Invariants: change only the rendering. Keep {LAYOUT_LOCK} and {SUBJECT_LOCK} exactly unchanged.

Avoid: color, gray fills, continuous contour lines, dotted points, thin sketch lines, inconsistent dash length or gaps, shadows, texture, scenery, props, labels, borders, logos, watermark, changed subjects, changed order, changed pose, or changed crop.
```

### Stage 2 targeted correction

```text
Line-style correction only. Preserve the exact canvas, layout, subjects, silhouettes, internal structure, positions, scale, spacing, and crop from Image 1.

Replace every remaining continuous contour with bold rounded short black dashes. Normalize dash length, stroke thickness, and gaps across the whole sheet. Remove all remaining color, gray, shading, texture, and background panels so every fill and background is pure white. Keep only pre-existing simple anatomical facial marks solid black; do not invent faces or details.
```

## Variables

- `{LAYOUT}`: concise description such as `a 3-column × 5-row edge-to-edge grid` or `one centered subject on a portrait canvas`.
- `{LAYOUT_LOCK}`: exact grid count, cell proportions, margins/gutters, alignment, crop behavior, and background segmentation observed in Image 1.
- `{SUBJECT_LOCK}`: subject list in reading order plus fixed pose, direction, and distinguishing features.
- `{BACKGROUND_RULE}`: for tiled art, preserve each tile and flatten it to one solid color; otherwise default to pure white unless the user requested another treatment.

