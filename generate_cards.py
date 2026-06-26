import os

# ============================================================
#  EDIT THIS CONFIG TO ADD/REMOVE/CHANGE SKILLS IN THE FUTURE
# ============================================================
CARDS = [
    {
        "name": "languages",
        "title": "LANGUAGES",
        "items": ["Dart", "Java", "C++"],
    },
    {
        "name": "frameworks",
        "title": "FRAMEWORKS & LIBRARIES",
        "items": ["Flutter", "GetX", "BLoC", "Dio"],
    },
    {
        "name": "databases",
        "title": "DATABASES",
        "items": ["Firebase", "SQLite"],
    },
    {
        "name": "tools",
        "title": "DESIGN & TOOLS",
        "items": ["GitHub", "Git", "VS Code", "Figma", "Postman"],
    },
    {
        "name": "workspace",
        "title": "WORKSPACE",
        "items": ["Windows", "Android Studio"],
    },
]

THEMES = {
    "dark": {
        "card_bg":    "#250b0f",
        "border":     "#442128",
        "title":      "#d99d87",
        "muted":      "#7b6261",
        "badge_fill": "#3a1520",
        "badge_text": "#999189",
        "frame":      "#d99d87",   # outer frame around each badge
    },
    "light": {
        "card_bg":    "#ffffff",
        "border":     "#CF7381",
        "title":      "#531C24",
        "muted":      "#795654",
        "badge_fill": "#fff0f2",
        "badge_text": "#531C24",
        "frame":      "#CF7381",
    },
}

BADGE_W   = 10    # horizontal padding inside badge
BADGE_H   = 26    # badge height
CHAR_W    = 7.5   # approx width per character (monospace)
FRAME_PAD = 4     # extra px around badge for the frame
GAP_X     = 12    # gap between badges horizontally
GAP_Y     = 10    # gap between badge rows
START_X   = 20
START_Y   = 60
MAX_W     = 320   # usable card width


def badge_width(text):
    return int(len(text) * CHAR_W + BADGE_W * 2)


def layout_rows(items):
    """Wrap items into rows that fit within MAX_W."""
    rows, row, row_w = [], [], 0
    for item in items:
        w = badge_width(item) + FRAME_PAD * 2 + GAP_X
        if row and row_w + w > MAX_W:
            rows.append(row)
            row, row_w = [], 0
        row.append(item)
        row_w += w
    if row:
        rows.append(row)
    return rows


def make_svg(card, theme):
    c = THEMES[theme]
    rows = layout_rows(card["items"])
    n_rows = len(rows)
    height = START_Y + n_rows * (BADGE_H + GAP_Y) + FRAME_PAD * 2 + 28

    badges_svg = []
    y = START_Y
    for row in rows:
        x = START_X
        for text in row:
            bw = badge_width(text)
            fw = bw + FRAME_PAD * 2
            fh = BADGE_H + FRAME_PAD * 2
            fx = x
            fy = y - FRAME_PAD
            bx = x + FRAME_PAD
            by = y
            tx = bx + bw // 2
            ty = y + BADGE_H // 2 + 4

            badges_svg.append(
                f'  <!-- frame -->'
                f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="9" ry="9"'
                f' fill="none" stroke="{c["frame"]}" stroke-width="1" opacity="0.55"/>'
                f'  <!-- badge -->'
                f'<rect x="{bx}" y="{by}" width="{bw}" height="{BADGE_H}" rx="6" ry="6"'
                f' fill="{c["badge_fill"]}"/>'
                f'<text x="{tx}" y="{ty}" font-family="monospace" font-size="12"'
                f' fill="{c["badge_text"]}" text-anchor="middle">{text}</text>'
            )
            x += fw + GAP_X

        y += BADGE_H + GAP_Y + FRAME_PAD

    svg = f'''<svg width="360" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="{height}" rx="14" ry="14" fill="{c["card_bg"]}" stroke="{c["border"]}" stroke-width="1.5"/>
  <text x="20" y="32" font-family="monospace" font-size="11" fill="{c["muted"]}" letter-spacing="2">{card["title"]}</text>
  <line x1="20" y1="42" x2="340" y2="42" stroke="{c["border"]}" stroke-width="1"/>
  {"".join(badges_svg)}
</svg>'''
    return svg


for theme in ("dark", "light"):
    os.makedirs(f"cards/{theme}", exist_ok=True)
    for card in CARDS:
        svg = make_svg(card, theme)
        path = f"cards/{theme}/{card['name']}.svg"
        with open(path, "w") as f:
            f.write(svg)
        print(f"  ✦ {path}")

print("\nDone ✦")
