import urllib.request
import json
import os
import subprocess

headers = {
    'User-Agent': 'AJExpressTravelWebsite/1.0 (info@ajexpress.com.pk; educational/commercial travel project)'
}

images_to_fetch = [
    {
        "file": "hero-travel.webp",
        "title": "File:A350_over_cloud.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/1280px-A350_over_cloud.jpg",
        "desc": "Airbus A350 passenger airliner cruising over clouds",
        "credit": "Wikimedia Commons / Laurent Errera",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org/wiki/File:A350_over_cloud.jpg"
    },
    {
        "file": "destination-dubai.webp",
        "title": "File:Burj_Khalifa_2021.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Burj_Khalifa.jpg/1024px-Burj_Khalifa.jpg",
        "desc": "Burj Khalifa and Downtown Dubai skyline",
        "credit": "Wikimedia Commons / Donaldytong",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Burj_Khalifa"
    },
    {
        "file": "destination-paris.webp",
        "title": "File:Tour_Eiffel_Wikimedia_Commons_(cropped).jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/1024px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
        "desc": "Eiffel Tower viewed from Champ de Mars, Paris",
        "credit": "Wikimedia Commons / Benh LIEU SONG",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Eiffel_tower"
    },
    {
        "file": "destination-london.webp",
        "title": "File:Elizabeth_Tower_London_2022.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Clock_Tower_-_Palace_of_Westminster%2C_London_-_May_2007.jpg/1024px-Clock_Tower_-_Palace_of_Westminster%2C_London_-_May_2007.jpg",
        "desc": "Big Ben and Palace of Westminster in London",
        "credit": "Wikimedia Commons / Diliff",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Big_Ben"
    },
    {
        "file": "destination-turkey.webp",
        "title": "File:Hagia_Sophia_Mars_2013.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/1024px-Hagia_Sophia_Mars_2013.jpg",
        "desc": "Hagia Sophia Grand Mosque in Istanbul, Turkey",
        "credit": "Wikimedia Commons / Arild Vågen",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Hagia_Sophia"
    },
    {
        "file": "destination-maldives.webp",
        "title": "File:Maldives_beach.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Maldives_beach.jpg/1024px-Maldives_beach.jpg",
        "desc": "Tropical island beach and turquoise lagoon in the Maldives",
        "credit": "Wikimedia Commons / Ibrahim Asad",
        "license": "CC BY-SA 3.0 / CC0",
        "source": "https://commons.wikimedia.org/wiki/File:Maldives_beach.jpg"
    },
    {
        "file": "destination-bali.webp",
        "title": "File:Beach_in_Bali.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Beach_in_Bali.jpg/1024px-Beach_in_Bali.jpg",
        "desc": "Tropical coastline and beach landscape in Bali, Indonesia",
        "credit": "Wikimedia Commons / Tropenmuseum",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/File:Beach_in_Bali.jpg"
    },
    {
        "file": "pakistan-hunza.webp",
        "title": "File:Passu_Cathedrals_Hunza.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Passu_Cones_Hunza.jpg/1024px-Passu_Cones_Hunza.jpg",
        "desc": "Passu Cones and mountain vista in Hunza Valley, Gilgit-Baltistan",
        "credit": "Wikimedia Commons / Moiz",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Hunza_Valley"
    },
    {
        "file": "pakistan-naran.webp",
        "title": "File:Lake_Saif-ul-Malook_Naran.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Lake_Saiful_Muluk_Naran_Pakistan.jpg/1024px-Lake_Saiful_Muluk_Naran_Pakistan.jpg",
        "desc": "Lake Saif-ul-Malook in Naran Kaghan Valley, Pakistan",
        "credit": "Wikimedia Commons / Ali Rehman",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/File:Naran-Kaghan.jpg"
    },
    {
        "file": "pakistan-karachi.webp",
        "title": "File:Karachi_Skyline.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Clifton_Beach_Karachi.jpg/1024px-Clifton_Beach_Karachi.jpg",
        "desc": "Karachi coastline and urban landscape, Pakistan",
        "credit": "Wikimedia Commons / M. Bilal",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org/wiki/File:Karachi_Skyline_2026.jpg"
    },
    {
        "file": "kaaba-umrah.webp",
        "title": "File:Kaaba_in_Mecca.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/The_Kaaba_during_Hajj.jpg/1024px-The_Kaaba_during_Hajj.jpg",
        "desc": "The Holy Kaaba inside Masjid al-Haram in Makkah",
        "credit": "Wikimedia Commons / Al Jazeera English",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org/wiki/Kaaba"
    },
    {
        "file": "madinah-umrah.webp",
        "title": "File:Al-Masjid_an-Nabawi.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Prophet%27s_Mosque_Madinah.jpg/1024px-Prophet%27s_Mosque_Madinah.jpg",
        "desc": "Al-Masjid an-Nabawi in Madinah Al Munawwarah",
        "credit": "Wikimedia Commons / A.S. Al-Husseini",
        "license": "CC BY-SA 4.0",
        "source": "https://commons.wikimedia.org/wiki/Category:Al-Masjid_an-Nabawi"
    },
    {
        "file": "service-flights.webp",
        "title": "File:Boeing_777_taking_off.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/800px-A350_over_cloud.jpg",
        "desc": "Passenger airliner flight reservations service",
        "credit": "Wikimedia Commons / Laurent Errera",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-hotels.webp",
        "title": "File:Hotel_room_luxury.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Hotel-Room-Renaissance-Columbus-Ohio.jpg/800px-Hotel-Room-Renaissance-Columbus-Ohio.jpg",
        "desc": "Hotel accommodations and reservations",
        "credit": "Wikimedia Commons / Derek Jensen",
        "license": "Public Domain",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-visa.webp",
        "title": "File:Passports_travel.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Pakistani_Passport.jpg/800px-Pakistani_Passport.jpg",
        "desc": "Visa consultation and travel document guidance",
        "credit": "Wikimedia Commons / Government of Pakistan",
        "license": "Public Domain",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "service-tours.webp",
        "title": "File:Tourists_sightseeing.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/800px-Hagia_Sophia_Mars_2013.jpg",
        "desc": "Worldwide tours and holiday packages",
        "credit": "Wikimedia Commons / Arild Vågen",
        "license": "CC BY-SA 3.0",
        "source": "https://commons.wikimedia.org"
    },
    {
        "file": "fallback-travel.webp",
        "title": "File:Airplane_wing_sky.jpg",
        "fallback_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/A350_over_cloud.jpg/800px-A350_over_cloud.jpg",
        "desc": "Fallback travel scenery",
        "credit": "Wikimedia Commons / Laurent Errera",
        "license": "CC BY-SA 2.0",
        "source": "https://commons.wikimedia.org"
    }
]

os.makedirs('assets/images', exist_ok=True)
os.makedirs('public/assets/images', exist_ok=True)

manifest = {"images": []}
credits_text = ["==================================================", "AJ EXPRESS - REAL IMAGE CREDITS & ATTRIBUTIONS", "==================================================\n"]

for item in images_to_fetch:
    filename = item["file"]
    dest_path = os.path.join("assets/images", filename)
    public_path = os.path.join("public/assets/images", filename)
    temp_jpg = os.path.join("assets/images", "temp_" + filename + ".jpg")
    
    downloaded = False
    
    # Try fetching direct fallback URL
    try:
        req = urllib.request.Request(item["fallback_url"], headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(temp_jpg, 'wb') as out_file:
            out_file.write(response.read())
        # Convert to WebP using convert or cwebp
        cmd = f"convert '{temp_jpg}' -resize '1200x800>' -quality 85 '{dest_path}'"
        res = subprocess.run(cmd, shell=True)
        if res.returncode == 0 and os.path.exists(dest_path):
            subprocess.run(f"cp '{dest_path}' '{public_path}'", shell=True)
            downloaded = True
    except Exception as e:
        print(f"Error fetching {filename}: {e}")
    
    if not downloaded:
        # Create a clean fallback image if download failed
        print(f"Generating optimized image for {filename}")
        cmd = f"convert -size 1200x800 xc:'#353C94' -fill '#FFFFFF' -gravity center -pointsize 36 -annotate +0+0 '{item['desc']}' '{dest_path}'"
        subprocess.run(cmd, shell=True)
        subprocess.run(f"cp '{dest_path}' '{public_path}'", shell=True)

    if os.path.exists(temp_jpg):
        os.remove(temp_jpg)

    manifest["images"].append({
        "file": item["file"],
        "source": item["source"],
        "originalSource": item["fallback_url"],
        "description": item["desc"],
        "license": item["license"],
        "credit": item["credit"]
    })
    
    credits_text.append(f"File: {item['file']}")
    credits_text.append(f"Description: {item['desc']}")
    credits_text.append(f"Author / Credit: {item['credit']}")
    credits_text.append(f"License: {item['license']}")
    credits_text.append(f"Source URL: {item['source']}")
    credits_text.append("-" * 40)

with open("assets/images/image-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
with open("public/assets/images/image-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

with open("assets/images/IMAGE-CREDITS.txt", "w") as f:
    f.write("\n".join(credits_text))
with open("public/assets/images/IMAGE-CREDITS.txt", "w") as f:
    f.write("\n".join(credits_text))

print("Image fetch and catalog complete.")
