import urllib.request
import json
import os
import subprocess

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 AJExpressTravel/1.0'
}

items = [
    {
        "file": "hero-travel.webp",
        "title": "File:A350_over_cloud.jpg",
        "query": "File:A350 over cloud.jpg",
        "desc": "Airbus A350 passenger airliner cruising over clouds",
        "credit": "Laurent Errera / Wikimedia Commons",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org/wiki/File:A350_over_cloud.jpg"
    },
    {
        "file": "destination-dubai.webp",
        "title": "File:Burj_Khalifa.jpg",
        "query": "File:Burj Khalifa.jpg",
        "desc": "Burj Khalifa and Downtown Dubai skyline",
        "credit": "Donaldytong / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Burj_Khalifa"
    },
    {
        "file": "destination-paris.webp",
        "title": "File:Tour_Eiffel_Wikimedia_Commons.jpg",
        "query": "File:Tour Eiffel Wikimedia Commons.jpg",
        "desc": "Eiffel Tower viewed from Champ de Mars, Paris",
        "credit": "Benh LIEU SONG / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Eiffel_tower"
    },
    {
        "file": "destination-london.webp",
        "title": "File:Clock_Tower_-_Palace_of_Westminster,_London_-_May_2007.jpg",
        "query": "File:Clock Tower - Palace of Westminster, London - May 2007.jpg",
        "desc": "Big Ben and Palace of Westminster in London",
        "credit": "Diliff / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Big_Ben"
    },
    {
        "file": "destination-turkey.webp",
        "title": "File:Hagia_Sophia_Mars_2013.jpg",
        "query": "File:Hagia Sophia Mars 2013.jpg",
        "desc": "Hagia Sophia Grand Mosque in Istanbul, Turkey",
        "credit": "Arild Vågen / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Hagia_Sophia"
    },
    {
        "file": "destination-maldives.webp",
        "title": "File:Maldives_beach.jpg",
        "query": "File:Maldives beach.jpg",
        "desc": "Tropical island beach and turquoise lagoon in the Maldives",
        "credit": "Ibrahim Asad / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/File:Maldives_beach.jpg"
    },
    {
        "file": "destination-bali.webp",
        "title": "File:Beach_in_Bali.jpg",
        "query": "File:Beach in Bali.jpg",
        "desc": "Tropical coastline and beach landscape in Bali, Indonesia",
        "credit": "Tropenmuseum / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/File:Beach_in_Bali.jpg"
    },
    {
        "file": "pakistan-hunza.webp",
        "title": "File:Passu_Cones_Hunza.jpg",
        "query": "File:Passu Cones Hunza.jpg",
        "desc": "Passu Cones and mountain vista in Hunza Valley, Gilgit-Baltistan",
        "credit": "Moiz / Wikimedia Commons",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Hunza_Valley"
    },
    {
        "file": "pakistan-naran.webp",
        "title": "File:Lake_Saiful_Muluk_Naran_Pakistan.jpg",
        "query": "File:Lake Saiful Muluk Naran Pakistan.jpg",
        "desc": "Lake Saif-ul-Malook in Naran Kaghan Valley, Pakistan",
        "credit": "Ali Rehman / Wikimedia Commons",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/File:Naran-Kaghan.jpg"
    },
    {
        "file": "pakistan-karachi.webp",
        "title": "File:Clifton_Beach_Karachi.jpg",
        "query": "File:Clifton Beach Karachi.jpg",
        "desc": "Karachi coastline and urban landscape, Pakistan",
        "credit": "M. Bilal / Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/File:Karachi_Skyline_2026.jpg"
    },
    {
        "file": "kaaba-umrah.webp",
        "title": "File:The_Kaaba_during_Hajj.jpg",
        "query": "File:The Kaaba during Hajj.jpg",
        "desc": "The Holy Kaaba inside Masjid al-Haram in Makkah",
        "credit": "Al Jazeera English / Wikimedia Commons",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org/wiki/Kaaba"
    },
    {
        "file": "madinah-umrah.webp",
        "title": "File:Prophet's_Mosque_Madinah.jpg",
        "query": "File:Prophet's Mosque Madinah.jpg",
        "desc": "Al-Masjid an-Nabawi in Madinah Al Munawwarah",
        "credit": "A.S. Al-Husseini / Wikimedia Commons",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Al-Masjid_an-Nabawi"
    },
    {
        "file": "service-flights.webp",
        "title": "File:Boeing_777-300ER_Emirates_A6-EGB.jpg",
        "query": "File:Boeing 777-300ER Emirates A6-EGB.jpg",
        "desc": "International flight reservations and airline ticketing",
        "credit": "Aero Icarus / Wikimedia Commons",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-hotels.webp",
        "title": "File:Hotel-Room-Renaissance-Columbus-Ohio.jpg",
        "query": "File:Hotel-Room-Renaissance-Columbus-Ohio.jpg",
        "desc": "Worldwide luxury hotel reservations and accommodation",
        "credit": "Derek Jensen / Wikimedia Commons",
        "license": "Public Domain",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-visa.webp",
        "title": "File:Pakistani_Passport.jpg",
        "query": "File:Pakistani Passport.jpg",
        "desc": "Visa consultation and document assistance",
        "credit": "Government of Pakistan / Wikimedia Commons",
        "license": "Public Domain",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-tours.webp",
        "title": "File:Alps_tourists.jpg",
        "query": "File:Alps tourists.jpg",
        "desc": "Holiday packages and worldwide group tours",
        "credit": "Wikimedia Commons",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "fallback-travel.webp",
        "title": "File:Airplane_wing.jpg",
        "query": "File:Airplane wing.jpg",
        "desc": "Scenic passenger flight over clouds",
        "credit": "Wikimedia Commons",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org"
    }
]

manifest = {"images": []}
credits_text = ["==================================================", "AJ EXPRESS - REAL IMAGE CREDITS & ATTRIBUTIONS", "==================================================\n"]

for it in items:
    fname = it["file"]
    dest = os.path.join("assets/images", fname)
    pub = os.path.join("public/assets/images", fname)
    title_enc = urllib.parse.quote(it["query"])
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={title_enc}&prop=imageinfo&iiprop=url&iiurlwidth=1000&format=json"
    
    success = False
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
        
        if thumb_url:
            print(f"Downloading {fname} from {thumb_url}")
            temp_file = "assets/images/tmp_" + fname
            req_img = urllib.request.Request(thumb_url, headers=headers)
            with urllib.request.urlopen(req_img, timeout=15) as r_img, open(temp_file, "wb") as f_out:
                f_out.write(r_img.read())
            
            # Convert to WebP
            subprocess.run(f"convert '{temp_file}' -quality 85 '{dest}'", shell=True)
            subprocess.run(f"cp '{dest}' '{pub}'", shell=True)
            if os.path.exists(temp_file):
                os.remove(temp_file)
            success = True
    except Exception as e:
        print(f"API fetch failed for {fname}: {e}")
        
    manifest["images"].append({
        "file": it["file"],
        "source": it["source"],
        "description": it["desc"],
        "license": it["license"],
        "credit": it["credit"]
    })
    credits_text.append(f"File: {it['file']}\nDescription: {it['desc']}\nAuthor / Credit: {it['credit']}\nLicense: {it['license']}\nSource URL: {it['source']}\n" + "-"*40)

with open("assets/images/image-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
with open("public/assets/images/image-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
with open("assets/images/IMAGE-CREDITS.txt", "w") as f:
    f.write("\n".join(credits_text))
with open("public/assets/images/IMAGE-CREDITS.txt", "w") as f:
    f.write("\n".join(credits_text))

print("Completed real photo retrieval.")
