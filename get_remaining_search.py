import urllib.request
import json
import time
import os
import subprocess

headers = {'User-Agent': 'AJExpressTravel/1.0 (Travel Agency Karachi, info@ajexpress.com.pk)'}

searches = {
    "hero-travel.webp": "Airbus A350 in flight sky",
    "destination-dubai.webp": "Burj Khalifa Dubai skyline",
    "pakistan-hunza.webp": "Passu Cones Hunza valley",
    "pakistan-naran.webp": "Saif ul Malook Lake Naran",
    "madinah-umrah.webp": "Al Masjid an Nabawi Madinah mosque",
    "service-flights.webp": "Commercial airplane taking off runway",
    "service-hotels.webp": "Luxury hotel suite bedroom",
    "service-tours.webp": "Tourists sightseeing landmark",
    "fallback-travel.webp": "Airplane wing above clouds sunset"
}

for fname, q in searches.items():
    dest = os.path.join("assets/images", fname)
    pub = os.path.join("public/assets/images", fname)
    q_enc = urllib.parse.quote(q)
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={q_enc}&gsrlimit=1&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json"
    try:
        print(f"Searching for {q}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        thumb_url = None
        for pid, page in pages.items():
            if "imageinfo" in page and len(page["imageinfo"]) > 0:
                thumb_url = page["imageinfo"][0].get("thumburl") or page["imageinfo"][0].get("url")
                break
        if thumb_url:
            print(f"Downloading {fname} from {thumb_url}")
            temp_file = "assets/images/tmp_" + fname
            req_img = urllib.request.Request(thumb_url, headers=headers)
            with urllib.request.urlopen(req_img, timeout=20) as r_img, open(temp_file, "wb") as f_out:
                f_out.write(r_img.read())
            subprocess.run(f"convert '{temp_file}' -resize '1400x900>' -quality 82 '{dest}'", shell=True)
            subprocess.run(f"cp '{dest}' '{pub}'", shell=True)
            if os.path.exists(temp_file):
                os.remove(temp_file)
        time.sleep(2)
    except Exception as e:
        print(f"Failed {fname}: {e}")

print("Remaining downloads finished.")
