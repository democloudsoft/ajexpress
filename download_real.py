import urllib.request
import json
import time
import os
import subprocess

headers = {'User-Agent': 'AJExpressTravelProductionSite/1.0 (Karachi Pakistan travel website; contact: info@ajexpress.com.pk)'}

# Direct high quality public domain / creative commons image links
direct_sources = {
    "hero-travel.webp": "https://upload.wikimedia.org/wikipedia/commons/6/64/A350_over_cloud.jpg",
    "destination-dubai.webp": "https://upload.wikimedia.org/wikipedia/commons/9/93/Burj_Khalifa.jpg",
    "pakistan-hunza.webp": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Passu_Cones_Hunza.jpg",
    "pakistan-naran.webp": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Lake_Saiful_Muluk_Naran_Pakistan.jpg",
    "madinah-umrah.webp": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Prophet%27s_Mosque_Madinah.jpg",
    "service-flights.webp": "https://upload.wikimedia.org/wikipedia/commons/6/64/A350_over_cloud.jpg",
    "service-hotels.webp": "https://upload.wikimedia.org/wikipedia/commons/5/56/Hotel-Room-Renaissance-Columbus-Ohio.jpg",
    "fallback-travel.webp": "https://upload.wikimedia.org/wikipedia/commons/6/64/A350_over_cloud.jpg"
}

for fname, url in direct_sources.items():
    dest = os.path.join("assets/images", fname)
    pub = os.path.join("public/assets/images", fname)
    temp = f"assets/images/tmp_{fname}.jpg"
    try:
        print(f"Fetching {fname}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as r, open(temp, "wb") as f:
            f.write(r.read())
        subprocess.run(f"convert '{temp}' -resize '1400x900>' -quality 82 '{dest}'", shell=True)
        subprocess.run(f"cp '{dest}' '{pub}'", shell=True)
        if os.path.exists(temp):
            os.remove(temp)
        time.sleep(1.5)
    except Exception as e:
        print(f"Error {fname}: {e}")

print("Direct download complete.")
