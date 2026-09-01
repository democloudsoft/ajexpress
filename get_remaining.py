import urllib.request
import json
import os
import subprocess

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AJExpress/1.0'}

queries = {
    "hero-travel.webp": "File:A350-941 (F-WXWB) Airbus (43790596324).jpg",
    "destination-dubai.webp": "File:Burj Khalifa Dubai 2019.jpg",
    "pakistan-hunza.webp": "File:Passu Cones - Gojal - Hunza.jpg",
    "pakistan-naran.webp": "File:Saiful Malook Lake (2018).jpg",
    "madinah-umrah.webp": "File:Prophet's Mosque in Medina, Saudi Arabia.jpg",
    "service-flights.webp": "File:Qatar Airways A350-900 (A7-ALA) (16521575822).jpg",
    "service-hotels.webp": "File:Grand Hotel Palace Rome suite.jpg",
    "service-tours.webp": "File:Tourists in Rome Colosseum.jpg",
    "fallback-travel.webp": "File:View from airplane window over clouds.jpg"
}

for fname, q in queries.items():
    dest = os.path.join("assets/images", fname)
    title_enc = urllib.parse.quote(q)
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={title_enc}&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json"
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        thumb_url = None
        for pid, page in pages.items():
            if "imageinfo" in page and len(page["imageinfo"]) > 0:
                thumb_url = page["imageinfo"][0].get("thumburl") or page["imageinfo"][0].get("url")
                break
        if not thumb_url:
            # try search query
            search_api = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(fname.replace('.webp', '').replace('-', ' '))}&gsrlimit=1&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json"
            req2 = urllib.request.Request(search_api, headers=headers)
            with urllib.request.urlopen(req2, timeout=10) as r2:
                d2 = json.loads(r2.read().decode('utf-8'))
            pages2 = d2.get("query", {}).get("pages", {})
            for pid, page in pages2.items():
                if "imageinfo" in page and len(page["imageinfo"]) > 0:
                    thumb_url = page["imageinfo"][0].get("thumburl") or page["imageinfo"][0].get("url")
                    break
        if thumb_url:
            print(f"Downloading {fname} from {thumb_url}")
            temp_file = "assets/images/tmp_" + fname
            req_img = urllib.request.Request(thumb_url, headers=headers)
            with urllib.request.urlopen(req_img, timeout=15) as r_img, open(temp_file, "wb") as f_out:
                f_out.write(r_img.read())
            subprocess.run(f"convert '{temp_file}' -resize '1400x900>' -quality 82 '{dest}'", shell=True)
            subprocess.run(f"cp '{dest}' 'public/assets/images/{fname}'", shell=True)
            if os.path.exists(temp_file):
                os.remove(temp_file)
    except Exception as e:
        print(f"Error {fname}: {e}")

print("Done remaining.")
