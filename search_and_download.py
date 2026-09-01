import urllib.request
import json
import os
import subprocess
import time

headers = {'User-Agent': 'AJExpressTravelProductionSite/1.0 (info@ajexpress.com.pk)'}

queries = {
    "hero-travel.webp": "Airbus A350 in flight",
    "destination-dubai.webp": "Burj Khalifa Dubai",
    "pakistan-hunza.webp": "Hunza Valley Pakistan",
    "pakistan-naran.webp": "Saiful Muluk Lake",
    "madinah-umrah.webp": "Prophet Mosque Madinah",
    "service-flights.webp": "Commercial airplane takeoff",
    "service-hotels.webp": "Hotel room suite",
    "service-tours.webp": "Sightseeing tourists landmark",
    "fallback-travel.webp": "Airplane view clouds"
}

for fname, q in queries.items():
    search_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(q)}&srnamespace=6&srlimit=1&format=json"
    try:
        req = urllib.request.Request(search_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            res = json.loads(r.read().decode('utf-8'))
        results = res.get("query", {}).get("search", [])
        if not results:
            print(f"No search results for {q}")
            continue
        title = results[0]["title"]
        print(f"Found title for {q}: {title}")
        
        info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"
        req2 = urllib.request.Request(info_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=10) as r2:
            res2 = json.loads(r2.read().decode('utf-8'))
        pages = res2.get("query", {}).get("pages", {})
        for pid, p in pages.items():
            img_url = p["imageinfo"][0]["url"]
            print(f"Downloading {fname} from {img_url}")
            temp = f"assets/images/tmp_{fname}"
            req3 = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(req3, timeout=30) as r3, open(temp, "wb") as f_out:
                f_out.write(r3.read())
            subprocess.run(f"convert '{temp}' -resize '1400x900>' -quality 82 'assets/images/{fname}'", shell=True)
            subprocess.run(f"cp 'assets/images/{fname}' 'public/assets/images/{fname}'", shell=True)
            if os.path.exists(temp):
                os.remove(temp)
            break
        time.sleep(1)
    except Exception as e:
        print(f"Error {fname}: {e}")

