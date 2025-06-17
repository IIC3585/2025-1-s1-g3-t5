import json
import os
import unicodedata
import re
from collections import defaultdict
from datetime import datetime

with open("autores.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

output_dir = "../../src/content/autores"
os.makedirs(output_dir, exist_ok=True)

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s]+", "-", text)

def format_array(arr):
    return "[" + ", ".join(f'"{x}"' for x in sorted(arr)) + "]"

autores = defaultdict(lambda: {
    "languages": set(),
    "occupation": set(),
    "genre": set()
})

# Agrega los datos a un diccionario
for item in raw_data:
    key = item["author"]
    entry = autores[key]
    entry["name"] = item["authorLabel"]         
    entry["slug"] = slugify(item["authorLabel"])
    
    birth_date_raw = item["birthDate"][:10]
    try:
        birth_date_obj = datetime.strptime(birth_date_raw, "%Y-%m-%d")
        entry["birthDate"] = birth_date_obj.strftime("%d-%m-%Y")
    except:
        entry["birthDate"] = birth_date_raw

    entry["placeOfBirth"] = item["placeOfBirthLabel"]
    entry["gender"] = item["genderLabel"]
    entry["country"] = "Chile"   
    entry["description"] = item["description"]
    entry["image"] = item["image"]
    entry["languages"].add(item["languageLabel"])
    entry["occupation"].add(item["occupationLabel"])
    entry["genre"].add(item["genreLabel"])

# Generación de los archivos .md 
# Le aisigné un id incremental, ya que intenté hacer las referencias 
# con el slug para el diseño de páginas, pero por algún motivo me tiraba 
# error como que no cumplía con el formato de la collection
count = 0
for idx, (key, entry) in enumerate(autores.items(), start=1):
    content = f"""---
id: {idx}
name: "{entry['name']}"
slug: "{entry['slug']}"
birthDate: "{entry['birthDate']}"
placeOfBirth: "{entry['placeOfBirth']}"
gender: "{entry['gender']}"
country: "{entry['country']}"
languages: {format_array(entry["languages"])}
occupation: {format_array(entry["occupation"])}
genre: {format_array(entry["genre"])}
image: "{entry['image']}"
description: "{entry['description']}"
---

{entry['description']}
"""
    path = f"{output_dir}/{idx}.md" 
    with open(path, "w", encoding="utf-8") as md_file:
        md_file.write(content)
    count += 1