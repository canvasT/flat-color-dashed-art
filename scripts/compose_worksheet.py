#!/usr/bin/env python3
"""Compose a tracing worksheet from accepted color and dashed masters."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


def ratio(value: str) -> float:
    parsed = float(value)
    if not 0 < parsed < 1:
        raise argparse.ArgumentTypeError("ratio must be greater than 0 and less than 1")
    return parsed


def content_crop(image: Image.Image, padding_ratio: float = 0.015) -> Image.Image:
    """Crop near-white outer whitespace while retaining a small safe padding."""
    rgb = image.convert("RGB")
    white = Image.new("RGB", rgb.size, "white")
    difference = ImageChops.difference(rgb, white).convert("L")
    mask = difference.point(lambda pixel: 255 if pixel > 10 else 0)
    bounds = mask.getbbox()
    if bounds is None:
        return rgb

    left, top, right, bottom = bounds
    padding = round(max(right - left, bottom - top) * padding_ratio)
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(rgb.width, right + padding)
    bottom = min(rgb.height, bottom + padding)
    return rgb.crop((left, top, right, bottom))


def fit(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
    if max_width < 1 or max_height < 1:
        raise ValueError("layout region is too small")
    scale = min(max_width / image.width, max_height / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.Resampling.LANCZOS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Place a large dashed drawing on white with a color reference at the upper right."
    )
    parser.add_argument("--color", required=True, type=Path, help="Accepted flat-color master")
    parser.add_argument("--outline", required=True, type=Path, help="Accepted dashed-outline master")
    parser.add_argument("--output", required=True, type=Path, help="New PNG worksheet path")
    parser.add_argument("--page-width", type=int, help="Output width; defaults to outline width")
    parser.add_argument("--page-height", type=int, help="Output height; defaults to outline height")
    parser.add_argument("--main-width", type=ratio, default=0.72, help="Main-art maximum width ratio")
    parser.add_argument("--main-height", type=ratio, default=0.76, help="Main-art maximum height ratio")
    parser.add_argument("--thumb-width", type=ratio, default=0.18, help="Color-thumbnail maximum width ratio")
    parser.add_argument("--thumb-height", type=ratio, default=0.17, help="Color-thumbnail maximum height ratio")
    parser.add_argument("--margin", type=ratio, default=0.04, help="Outer margin ratio")
    parser.add_argument("--force", action="store_true", help="Allow replacing an existing output")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.color.is_file():
        raise SystemExit(f"color image not found: {args.color}")
    if not args.outline.is_file():
        raise SystemExit(f"outline image not found: {args.outline}")
    if args.output.exists() and not args.force:
        raise SystemExit(f"output already exists: {args.output}; choose a versioned name or use --force")

    with Image.open(args.outline) as opened_outline:
        outline = content_crop(opened_outline)
        default_width, default_height = opened_outline.size
    with Image.open(args.color) as opened_color:
        color = content_crop(opened_color)

    page_width = args.page_width or default_width
    page_height = args.page_height or default_height
    if page_width < 64 or page_height < 64:
        raise SystemExit("page dimensions must both be at least 64 pixels")

    canvas = Image.new("RGB", (page_width, page_height), "white")
    main = fit(outline, round(page_width * args.main_width), round(page_height * args.main_height))
    thumbnail = fit(color, round(page_width * args.thumb_width), round(page_height * args.thumb_height))

    margin_x = round(page_width * args.margin)
    margin_y = round(page_height * args.margin)

    main_region_left = margin_x
    main_region_top = round(page_height * 0.18)
    main_region_width = round(page_width * args.main_width)
    main_region_height = round(page_height * args.main_height)
    main_x = main_region_left + max(0, (main_region_width - main.width) // 2)
    main_y = main_region_top + max(0, (main_region_height - main.height) // 2)

    thumb_x = page_width - margin_x - thumbnail.width
    thumb_y = margin_y

    canvas.paste(main, (main_x, main_y))
    canvas.paste(thumbnail, (thumb_x, thumb_y))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
