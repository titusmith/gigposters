# Gig Posters

An archive of gig posters on an endless, draggable canvas.

- `index.html`: the whole site (layout, interaction, search, light/dark switch) in one file.
- `posters/`: two WebP files per poster version: `<poster>.webp` (opened view, about 2000px on the long edge) and `<poster>-thumb.webp` (canvas, 400px on the short edge). Color versions add the color: `2026-9-25-al-pink.webp`, `2026-9-25-al-pink-thumb.webp`.
- `posters.csv`: one line per design: `poster, shape, colors, tags`. Shape is `portrait` or `landscape`; colors are paper colors separated by slashes (`pink/cream`), drawn from green, blue, red, orange, yellow, pink, purple, cream, white, grey; tags are separated by commas. Edit it right on GitHub when you upload new posters.

To run it locally, open `index.html` from a local web server (for example `python3 -m http.server`) so the images load.

## Planned
- Scanned posters (300dpi masters kept outside this repo; compressed web versions here).
