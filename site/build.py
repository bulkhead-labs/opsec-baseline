#!/usr/bin/env python3
"""Build the story page.

    python3 site/build.py                  # writes docs/index.html for GitHub Pages
    python3 site/build.py --preview OUT    # writes a self-contained page body (fonts inlined) to OUT

The source is site/story.html. Fonts are self-hosted from docs/fonts/, so
visitors' browsers make no third-party requests. The logo comes from assets/.
"""
import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WALLS = 7

# Brand fills in the lockup SVG, mapped to the page's colour tokens.
FILLS = {"#111417": "var(--text)", "#EC5A20": "var(--accent)", "#535B63": "var(--muted)"}

# The faces the page uses, latin subsets only for the preview.
PREVIEW_FONTS = [
    ("Big Shoulders Stencil Display", "normal", "800 900", "big-shoulders-stencil-display-800-900-latin.woff2"),
    ("Big Shoulders Display", "normal", "700 800", "big-shoulders-display-700-800-latin.woff2"),
    ("Atkinson Hyperlegible Next", "normal", "400 700", "atkinson-hyperlegible-next-400-700-latin.woff2"),
    ("Atkinson Hyperlegible Next", "italic", "400 700", "atkinson-hyperlegible-next-400-700-italic-latin.woff2"),
    ("JetBrains Mono", "normal", "400 600", "jetbrains-mono-400-600-latin.woff2"),
]


def hull(n: int) -> str:
    """The hull from above, cut into seven compartments. Walls before n are built,
    wall n is lit, the rest are outlines. n=0 shows none built; n=8 shows all."""
    w, gap, h = 10, 3, 22
    parts = []
    for i in range(1, WALLS + 1):
        cls = "c done" if i < n else "c lit" if i == n else "c"
        parts.append(f'<rect class="{cls}" x="{(i - 1) * (w + gap)}" y="0" width="{w}" height="{h}"/>')
    x = WALLS * (w + gap)
    bow = "bow done" if n > WALLS else "bow"
    parts.append(f'<path class="{bow}" d="M{x} 0 C{x + 8} 0 {x + 12} 6 {x + 16} 11 C{x + 12} 16 {x + 8} 22 {x} 22 Z"/>')
    label = (
        "A hull with seven compartments, none walled yet" if n == 0
        else "A hull with all seven walls in place" if n > WALLS
        else f"A hull with seven compartments; wall {n} of {WALLS} lit"
    )
    return (f'<svg class="hull" viewBox="-1 -1 {x + 18} {h + 2}" role="img" aria-label="{label}">'
            + "".join(parts) + "</svg>")


def logo() -> str:
    svg = (ROOT / "assets" / "bulkhead-lockup-light.svg").read_text()
    for hexv, var in FILLS.items():
        svg = svg.replace(f'fill="{hexv}"', f'style="fill:{var}"')
    return svg


def render(fonts: str) -> str:
    html = (ROOT / "site" / "story.html").read_text()
    html = html.replace("<!--FONTS-->", fonts).replace("<!--LOGO-->", logo())
    return re.sub(r"<!--HULL:(\d)-->", lambda m: hull(int(m.group(1))), html)


def preview_fonts() -> str:
    faces = []
    for family, style, weight, file in PREVIEW_FONTS:
        data = base64.b64encode((ROOT / "docs" / "fonts" / "woff2" / file).read_bytes()).decode()
        faces.append(f'@font-face{{font-family:"{family}";font-style:{style};font-weight:{weight};'
                     f'font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}')
    return "<style>" + "".join(faces) + "</style>"


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--preview":
        html = render(preview_fonts())
        # The preview host supplies its own document skeleton.
        html = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", html)
        html = re.sub(r'<meta (charset|name="viewport")[^>]*>\s*', "", html)
        html = re.sub(r"</head>\s*<body>\s*|</body>\s*</html>\s*", "", html)
        Path(sys.argv[2]).write_text(html)
        return
    out = ROOT / "docs" / "index.html"
    out.write_text(render('<link rel="stylesheet" href="fonts/fonts.css">'))
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
