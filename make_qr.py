import csv, qrcode, os

BASE = BASE = "https://vocalmate-support.github.io/l"
os.makedirs("qr", exist_ok=True)

count = 0
for r in csv.DictReader(open("songs.csv", encoding="utf-8")):
    slug = f"{r['slug']}-{r['key']}-{r['kind'][0]}"
    url = f"{BASE}/{slug}/"
    qr = qrcode.QRCode(box_size=12, border=3,
                       error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(f"qr/{slug}.png")
    print(f"{slug}  →  {url}")
    count += 1

print(f"\n{count} QR codes created.")