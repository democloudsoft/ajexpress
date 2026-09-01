import urllib.request
import json
import time
import os
import subprocess

headers = {'User-Agent': 'AJExpressTravel/1.0 (info@ajexpress.com.pk)'}

# Exact Wikimedia page titles
targets = [
    ("hero-travel.webp", "File:Airbus_A350-900_Delta_Air_Lines_(DAL)_N501DN_-_MSN_109_(cropped).jpg"),
    ("destination-dubai.webp", "File:Burj_Khalifa_and_Dubai_Mall_fountain_at_night.jpg"),
    ("pakistan-hunza.webp", "File:Passu_Cathedrals,_Hunza_Valley,_Northern_Pakistan.jpg"),
    ("pakistan-naran.webp", "File:Lake_Saiful_Muluk_Naran_Pakistan.jpg"),
    ("madinah-umrah.webp", "File:Masjid_Nabawi._Madinah,_Saudi_Arabia.jpg"),
    ("service-flights.webp", "File:Boeing_777-300ER_Emirates_A6-EGB.jpg"),
    ("service-hotels.webp", "File:The_May_Fair_Hotel_-_King_Studio.jpg"),
    ("service-tours.webp", "File:Grand_Canal_Venice_June_2013.jpg"),
    ("fallback-travel.webp", "File:Sunset_above_the_clouds_from_an_airplane.jpg")
]

for filename, title in targets:
    url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode('utf-8'))
        pages = data.get("query", {}).get("pages", {})
        thumb_url = None
        for pid, p in pages.items():
            if "imageinfo" in p and len(p["imageinfo"]) > 0:
                thumb_url = p["imageinfo"][0].get("thumburl") or p["imageinfo"][0].get("url")
                break
        
        if thumb_url:
            print(f"Got {filename} -> {thumb_url}")
            temp = f"assets/images/tmp_{filename}"
            req_img = urllib.request.Request(thumb_url, headers=headers)
            with urllib.request.urlopen(req_img, timeout=20) as r_img, open(temp, "wb") as f_out:
                f_out.write(r_img.read())
            subprocess.run(f"convert '{temp}' -resize '1400x900>' -quality 82 'assets/images/{filename}'", shell=True)
            subprocess.run(f"cp 'assets/images/{filename}' 'public/assets/images/{filename}'", shell=True)
            if os.path.exists(temp):
                os.remove(temp)
        else:
            print(f"No thumburl for {title}")
        time.sleep(1)
    except Exception as e:
        print(f"Failed {filename}: {e}")

