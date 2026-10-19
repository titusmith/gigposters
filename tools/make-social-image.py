# Rebuilds social.jpg (1200x630 link preview) from the posters in posters.csv.
# Usage: python3 tools/make-social-image.py . social.jpg   (needs Pillow)
import sys, random
from PIL import Image, ImageDraw, ImageFilter
repo, out = sys.argv[1], sys.argv[2]
W, H, BG = 1200, 630, (235, 235, 232)
designs = []
for l in open(repo + '/posters.csv'):
    s = l.strip()
    if not s or s.startswith('#') or s.lower().startswith('poster,'): continue
    p = [x.strip() for x in s.split(',')]
    cols = [c for c in p[2].split('/') if c]
    files = [f"{p[0]}-{c}.webp" for c in cols] if cols else [p[0] + '.webp']
    designs.append((p[0], p[1].startswith('l'), files))
rnd = random.Random(11)
pw = 176; ph = round(pw * 14 / 11); lw = ph; lh = pw
gap = 30; stride = lw + gap
canvas = Image.new('RGB', (W, H), BG)
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
placed = []
count = {}
x0 = -lw * 0.35
prev = set()
col = 0
x = x0
while x < W:
    y = -rnd.uniform(40, 220)
    used = set()
    while y < H:
        choices = [d for d in designs if d[0] not in used and d[0] not in prev] or designs
        least = min(count.get(d[0], 0) for d in choices)
        name, land, files = rnd.choice([d for d in choices if count.get(d[0], 0) == least])
        count[name] = count.get(name, 0) + 1
        used.add(name)
        w, h = (lw, lh) if land else (pw, ph)
        px = x + (lw - w) / 2
        placed.append((files[rnd.randrange(len(files))], int(px), int(y), w, h))
        y += h + gap
    prev = used; x += stride; col += 1
sd = ImageDraw.Draw(shadow)
for f, px, py, w, h in placed:
    sd.rounded_rectangle([px, py + 8, px + w, py + h + 8], 4, fill=(0, 0, 0, 46))
shadow = shadow.filter(ImageFilter.GaussianBlur(9))
canvas.paste(shadow, (0, 0), shadow)
for f, px, py, w, h in placed:
    im = Image.open(repo + '/posters/' + f).convert('RGB').resize((w, h), Image.LANCZOS)
    mask = Image.new('L', (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], 2, fill=255)
    canvas.paste(im, (px, py), mask)
canvas.save(out, 'JPEG', quality=86, optimize=True, progressive=True)
print(len(placed), 'posters')
