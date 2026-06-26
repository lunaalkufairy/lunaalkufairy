import os, html

CARDS = [
    {"name": "languages",  "title": "LANGUAGES",             "items": ["Dart", "Java", "C++"]},
    {"name": "frameworks", "title": "FRAMEWORKS & LIBRARIES", "items": ["Flutter", "GetX", "BLoC", "Dio"]},
    {"name": "databases",  "title": "DATABASES",              "items": ["Firebase", "SQLite"]},
    {"name": "tools",      "title": "DESIGN & TOOLS",         "items": ["GitHub", "Git", "VS Code", "Figma", "Postman"]},
    {"name": "workspace",  "title": "WORKSPACE",              "items": ["Windows", "Android Studio"]},
]

THEMES = {
    "dark":  {"card_bg":"#250b0f","border":"#442128","title":"#d99d87","muted":"#7b6261","badge_fill":"#3a1520","badge_text":"#999189","frame":"#d99d87","sep":"#3a1520"},
    "light": {"card_bg":"#ffffff","border":"#CF7381","title":"#531C24","muted":"#795654","badge_fill":"#fff0f2","badge_text":"#531C24","frame":"#CF7381","sep":"#f5dde0"},
}

ROW_H   = 44
PAD_TOP = 20
PAD_L   = 24
COL2_X  = 170
WIDTH   = 520

def make_combined(theme):
    c = THEMES[theme]
    h = PAD_TOP + len(CARDS) * ROW_H + PAD_TOP
    rows_svg = []
    for i, card in enumerate(CARDS):
        y = PAD_TOP + i * ROW_H
        items_str = html.escape("  ·  ".join(card["items"]))
        safe_title = html.escape(card["title"])
        # separator line (not after last row)
        if i > 0:
            rows_svg.append(f'<line x1="{PAD_L}" y1="{y}" x2="{WIDTH-PAD_L}" y2="{y}" stroke="{c["sep"]}" stroke-width="1"/>')
        # category label
        rows_svg.append(
            f'<text x="{PAD_L}" y="{y+26}" font-family="monospace" font-size="10" '
            f'fill="{c["muted"]}" letter-spacing="1.5">{safe_title}</text>'
        )
        # items
        rows_svg.append(
            f'<text x="{COL2_X}" y="{y+26}" font-family="monospace" font-size="12" '
            f'fill="{c["title"]}">{items_str}</text>'
        )

    return (
        f'<svg width="{WIDTH}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect width="{WIDTH}" height="{h}" rx="14" fill="{c["card_bg"]}" stroke="{c["border"]}" stroke-width="1.5"/>'
        + "".join(rows_svg)
        + '</svg>'
    )

os.makedirs("cards/dark", exist_ok=True)
os.makedirs("cards/light", exist_ok=True)

for theme in ("dark", "light"):
    svg = make_combined(theme)
    path = f"cards/{theme}/stack.svg"
    with open(path, "w") as f: f.write(svg)
    print(f"  ✦ {path}")

print("\nDone ✦")
