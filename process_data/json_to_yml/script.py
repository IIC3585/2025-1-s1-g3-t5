import os
import json
# la base de datos se obtuvo de: https://github.com/NinjasCL/chileanbirds-dataset/tree/master/data
# Cargar archivo JSON
with open("aves.json", "r", encoding="utf-8") as f:
    aves = json.load(f)

# Crear carpeta de salida
output_dir = "../../src/content/aves"
os.makedirs(output_dir, exist_ok=True)

count = 0
for idx, ave in enumerate(aves, start=1):
    data = ave.get("data", {})
    info = data.get("info", {})
    names = data.get("names", {})

    # Extraer campos requeridos
    uid = str(data.get("uid")).strip()
    spanish = names.get("spanish")
    latin = names.get("latin")
    english = names.get("english")
    image = data.get("image", {}).get("url")
    description = data.get("description")
    habitat = data.get("habitat")
    didyouknow = data.get("didyouknow")
    iucn_root = data.get("iucn")  # este es el iucn correcto
    size = info.get("size", {}).get("value")
    geo = info.get("geo", {}).get("value")

    # Verificar si algún campo requerido está vacío o ausente
    required_fields = [uid, spanish, latin, english, image, description, habitat, didyouknow, iucn_root, size, geo]
    if not all(required_fields):
        continue
    # Generar contenido YML
    content = f"""uid: "{uid}"
        spanishName: "{spanish}"
        latinName: "{latin}"
        englishName: "{english}"
        image: "{image}"
        description: "{description}"
        habitat: "{habitat}"
        didyouknow: "{didyouknow}"
        iucn: "{iucn_root}"
        size: "{size}"
        geo: "{geo}"
        """

    # Guardar archivo
    filepath = os.path.join(output_dir, f"{uid}.yaml")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    count += 1
