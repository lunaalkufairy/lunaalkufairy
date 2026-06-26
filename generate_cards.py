import os, html

CARDS = [
    {"name": "languages",  "title": "LANGUAGES",             "items": ["Dart", "Java", "C++"]},
    {"name": "frameworks", "title": "FRAMEWORKS & LIBRARIES", "items": ["Flutter", "GetX", "BLoC", "Dio"]},
    {"name": "databases",  "title": "DATABASES",              "items": ["Firebase", "SQLite"]},
    {"name": "tools",      "title": "DESIGN & TOOLS",         "items": ["GitHub", "Git", "VS Code", "Figma", "Postman"]},
    {"name": "workspace",  "title": "WORKSPACE",              "items": ["Windows", "Android Studio"]},
]

THEMES = {
    "dark":  {"card_bg":"#250b0f","border":"#442128","title":"#d99d87","muted":"#7b6261","badge_fill":"#3a1520","badge_text":"#999189","frame":"#d99d87"},
    "light": {"card_bg":"#ffffff","border":"#CF7381","title":"#531C24","muted":"#795654","badge_fill":"#fff0f2","badge_text":"#531C24","frame":"#CF7381"},
}

BADGE_H=26; CHAR_W=7.5; PAD_X=10; FRAME=4; GAP_X=12; GAP_Y=10; START_X=20; START_Y=60; MAX_W=320

def bw(t): return int(len(t)*CHAR_W + PAD_X*2)

def rows(items):
    result, row, w = [], [], 0
    for it in items:
        fw = bw(it)+FRAME*2+GAP_X
        if row and w+fw > MAX_W: result.append(row); row, w = [], 0
        row.append(it); w += fw
    if row: result.append(row)
    return result

def make_svg(card, theme):
    c = THEMES[theme]
    rws = rows(card["items"])
    h = START_Y + len(rws)*(BADGE_H+GAP_Y+FRAME) + 28
    badges = []
    y = START_Y
    for row in rws:
        x = START_X
        for t in row:
            fw = bw(t)+FRAME*2; fh = BADGE_H+FRAME*2
            badges.append(
                f'<rect x="{x}" y="{y-FRAME}" width="{fw}" height="{fh}" rx="9" fill="none" stroke="{c["frame"]}" stroke-width="1" opacity="0.55"/>'
                f'<rect x="{x+FRAME}" y="{y}" width="{bw(t)}" height="{BADGE_H}" rx="6" fill="{c["badge_fill"]}"/>'
                f'<text x="{x+FRAME+bw(t)//2}" y="{y+BADGE_H//2+4}" font-family="monospace" font-size="12" fill="{c["badge_text"]}" text-anchor="middle">{html.escape(t)}</text>'
            )
            x += fw+GAP_X
        y += BADGE_H+GAP_Y+FRAME

    # escape & in title for valid XML
    safe_title = html.escape(card["title"])
    return (f'<svg width="360" height="{h}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="360" height="{h}" rx="14" fill="{c["card_bg"]}" stroke="{c["border"]}" stroke-width="1.5"/>'
            f'<text x="20" y="32" font-family="monospace" font-size="11" fill="{c["muted"]}" letter-spacing="2">{safe_title}</text>'
            f'<line x1="20" y1="42" x2="340" y2="42" stroke="{c["border"]}" stroke-width="1"/>'
            + "".join(badges) + '</svg>')

for theme in ("dark","light"):
    os.makedirs(f"cards/{theme}", exist_ok=True)
    for card in CARDS:
        path = f"cards/{theme}/{card['name']}.svg"
        with open(path,"w") as f: f.write(make_svg(card, theme))
        print(f"  ✦ {path}")
print("\nDone ✦")
