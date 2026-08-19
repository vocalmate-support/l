import csv, os, html

OUT = "docs/s"
os.makedirs(OUT, exist_ok=True)

TPL = """<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>{title}</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace("{url}");</script>
</head><body>
<p>Redirecting to <a href="{url}">{title}</a>…</p>
</body></html>"""

for r in csv.DictReader(open("songs.csv", encoding="utf-8")):
    slug = f"{r['slug']}-{r['key']}-{r['kind'][0]}"
    url = f"https://www.youtube.com/watch?v={r['youtube_id']}"
    os.makedirs(f"{OUT}/{slug}", exist_ok=True)
    with open(f"{OUT}/{slug}/index.html", "w", encoding="utf-8") as f:
        f.write(TPL.format(url=url, title=html.escape(r['title'])))