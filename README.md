# Gig Posters

An archive of gig posters on an endless, draggable canvas.

- `index.html`: the whole site (layout, interaction, search, light/dark switch) in one file.
- `posters/`: web-sized poster images, named `YYYY-M-D-code.png`.

To run it locally, open `index.html` from a local web server (for example `python3 -m http.server`) so the images load.

## Planned
- Scanned posters (300dpi masters kept outside this repo; compressed web versions here).
- Color variants named `…_color.png`: treated as one design for tags and for no-repeat rules; search ignores color.
- Optional color filter circles above the search bar.
