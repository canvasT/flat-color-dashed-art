#!/usr/bin/env python3
"""Fit a raster image onto a white A4 canvas without cropping or distortion."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


A4_MM = (210, 297)
DEFAULT_DPI = 150


def a4_pixel_size(orientation: str, dpi: int) -> tuple[int, int]:
    short = round(A4_MM[0] / 25.4 * dpi)
    long = round(A4_MM[1] / 25.4 * dpi)
    return (short, long) if orientation == "portrait" else (long, short)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fit a complete image proportionally onto an A4 white canvas."
    )
    parser.add_argument("--input", required=True, type=Path, help="Source raster image")
    parser.add_argument("--output", required=True, type=Path, help="New A4 PNG path")
    parser.add_argument(
        "--orientation",
        choices=("portrait", "landscape"),
        default="portrait",
        help="A4 page orientation (default: portrait)",
    )
    parser.add_argument("--dpi", type=int, default=DEFAULT_DPI, help="A4 raster DPI (default: 150)")
    parser.add_argument("--force", action="store_true", help="Allow replacing an existing output")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"input image not found: {args.input}")
    if args.output.exists() and not args.force:
        raise SystemExit(f"output already exists: {args.output}; choose a versioned name or use --force")
    if args.dpi < 36 or args.dpi > 1200:
        raise SystemExit("dpi must be between 36 and 1200")

    page_width, page_height = a4_pixel_size(args.orientation, args.dpi)
    with Image.open(args.input) as opened:
        rgba = opened.convert("RGBA")
        background = Image.new("RGBA", rgba.size, "white")
        background.alpha_composite(rgba)
        source = background.convert("RGB")

    scale = min(page_width / source.width, page_height / source.height)
    fitted_size = (
        max(1, round(source.width * scale)),
        max(1, round(source.height * scale)),
    )
    fitted = source.resize(fitted_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (page_width, page_height), "white")
    position = ((page_width - fitted.width) // 2, (page_height - fitted.height) // 2)
    canvas.paste(fitted, position)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True, dpi=(args.dpi, args.dpi))


if __name__ == "__main__":
    main()
