import urllib.request
import json
import os
import subprocess

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

urls = {
    "hero-travel.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/1280px-A350_over_cloud.jpg",
    "destination-dubai.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Burj_Khalifa.jpg/800px-Burj_Khalifa.jpg",
    "pakistan-hunza.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Passu_Cones_Hunza.jpg/800px-Passu_Cones_Hunza.jpg",
    "pakistan-naran.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Lake_Saiful_Muluk_Naran_Pakistan.jpg/800px-Lake_Saiful_Muluk_Naran_Pakistan.jpg",
    "madinah-umrah.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Prophet%27s_Mosque_Madinah.jpg/800px-Prophet%27s_Mosque_Madinah.jpg",
    "service-flights.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/800px-A350_over_cloud.jpg",
    "service-hotels.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Hotel-Room-Renaissance-Columbus-Ohio.jpg/800px-Hotel-Room-Renaissance-Columbus-Ohio.jpg",
    "service-tours.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/800px-Hagia_Sophia_Mars_2013.jpg",
    "fallback-travel.webp": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/800px-A350_over_cloud.jpg"
}

for fname, u in urls.items():
    dest = f"assets/images/{fname}"
    pub = f"public/assets/images/{fname}"
    tmp = f"assets/images/t_{fname}.jpg"
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r, open(tmp, 'wb') as f:
            f.write(r.read())
        subprocess.run(f"convert '{tmp}' -resize '1200x800>' -quality 85 '{dest}'", shell=True)
        subprocess.run(f"cp '{dest}' '{pub}'", shell=True)
        if os.path.exists(tmp):
            os.remove(tmp)
        print(f"Successfully converted {fname}")
    except Exception as e:
        print(f"Error {fname}: {e}")

