# Render the 24 Nov 2026 world-news summary image (1024x1024 PNG).
# News researched 2026-11-25 from Reuters/AP/WSJ/Finnhub (see README).
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (11, 34, 57)
INK = (18, 28, 40)
GREY = (58, 68, 80)
LIGHT = (244, 246, 248)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

F_TITLE = font("DejaVuSans-Bold.ttf", 52)
F_DATE = font("DejaVuSans.ttf", 28)
F_KICK = font("DejaVuSans-Bold.ttf", 22)
F_HEAD = font("DejaVuSans-Bold.ttf", 34)
F_BODY = font("DejaVuSans.ttf", 25)
F_NUM = font("DejaVuSans-Bold.ttf", 44)
F_FOOT = font("DejaVuSans.ttf", 20)

STORIES = [
    {
        "color": (192, 57, 43),
        "kicker": "MARKETS",
        "head": "Nvidia whipsaws: -5.9% after +31.5%",
        "body": "A day after its biggest rally in 20 years on Huang's return as CEO, Nvidia fell 5.86% to $155.38; Nasdaq -1.48%.",
    },
    {
        "color": (142, 68, 173),
        "kicker": "TRADE",
        "head": "US readies new tariffs on 16 economies",
        "body": "USTR Greer is set to unveil Section 301 findings this week; EU, Japan and Korea capped at 15%, China faces more.",
    },
    {
        "color": (36, 113, 163),
        "kicker": "UKRAINE WAR",
        "head": "Ukraine drones sink Russian ship off Libya",
        "body": "Naval drones sank the corvette Merkury at Benghazi; Kyiv calls it self-defence, Tripoli condemns the strike.",
    },
    {
        "color": (185, 119, 14),
        "kicker": "MIDDLE EAST",
        "head": "Vance, Rubio meet Qatar PM on Iran talks",
        "body": "Qatar mediates as US-Iran talks stall; Trump says no deal is needed, as fears of renewed war grow.",
    },
    {
        "color": (17, 122, 101),
        "kicker": "TECH  ·  CHINA",
        "head": "US blacklists Megaspeed over Nvidia chips",
        "body": "Commerce puts the Singapore cloud firm and six affiliates on the Entity List, barring US AI-chip sales.",
    },
    {
        "color": (101, 67, 33),
        "kicker": "GAZA",
        "head": "Israel kills Hamas security chief in Gaza",
        "body": "An airstrike killed Naeem Abu Nahel, head of Hamas internal security, and six others in Gaza City.",
    },
]

def wrap(draw, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

# ---- header ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((48, 26), "THE WORLD TODAY", font=F_TITLE, fill=WHITE)
d.text((48, 96), "Tuesday, 24 November 2026  ·  Six stories that defined the day",
       font=F_DATE, fill=(196, 210, 224))

# ---- story bands ----
y = 148
band_h = (H - 148 - 36) // 6  # 36px footer
for i, s in enumerate(STORIES):
    y0 = y + i * band_h
    y1 = y0 + band_h
    bg = WHITE if i % 2 == 0 else LIGHT
    d.rectangle([0, y0, W, y1], fill=bg)
    # left number column
    d.rectangle([0, y0, 84, y1], fill=s["color"])
    num = str(i + 1)
    nw = d.textlength(num, font=F_NUM)
    d.text((42 - nw / 2, y0 + band_h / 2 - 30), num, font=F_NUM, fill=WHITE)
    # text
    tx = 112
    d.text((tx, y0 + 10), s["kicker"], font=F_KICK, fill=s["color"])
    d.text((tx, y0 + 38), s["head"], font=F_HEAD, fill=INK)
    lines = wrap(d, s["body"], F_BODY, W - tx - 48)
    ly = y0 + 84
    for ln in lines[:2]:
        d.text((tx, ly), ln, font=F_BODY, fill=GREY)
        ly += 31
    # divider
    if i < len(STORIES) - 1:
        d.line([0, y1, W, y1], fill=(214, 220, 226), width=1)

# ---- footer ----
fy = H - 36
d.rectangle([0, fy, W, H], fill=NAVY)
d.text((48, fy + 7),
       "Sources: Reuters, AP, WSJ, Finnhub  ·  Image: make.fun news-image-20261124",
       font=F_FOOT, fill=(196, 210, 224))

# ---- fit checks (fail loudly instead of silently truncating) ----
for s in STORIES:
    hw = d.textlength(s["head"], font=F_HEAD)
    assert hw <= W - 112 - 48, f"headline too long ({hw:.0f}px): {s['head']}"
    bl = wrap(d, s["body"], F_BODY, W - 112 - 48)
    assert len(bl) <= 2, f"body wraps to {len(bl)} lines: {s['body']}"
print("fit checks passed")

out = "/home/hatch/workspace/makefun-token-radar/news-image-20261124/entry.png"
img.save(out, "PNG", optimize=True)
import os
print("saved", os.path.getsize(out), "bytes")
print("size:", img.size)
