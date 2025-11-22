from transformers import pipeline
from PIL import Image
import json

# Clasificador de imágenes (bueno para animales)
detector = pipeline("image-classification", model="facebook/deit-base-patch16-224")

# Cargar imagen
imagen = Image.open("perro2.jpg").convert("RGB")

# Obtener predicciones (por ejemplo las 3 mejores)
predicciones = detector(imagen, top_k=3)

# Unimos todos los labels en un solo texto en minúsculas
labels_text = " ".join([p["label"].lower() for p in predicciones])

# Palabras clave para cada especie
perro_keywords = [
    "dog", "hound", "corgi", "beagle", "retriever", "terrier", "shepherd",
    "poodle", "bulldog", "chihuahua", "dachshund", "spaniel", "collie",
    "pinscher", "mastiff", "doberman"
]

gato_keywords = [
    "cat", "kitten", "siamese", "persian"
]

ave_keywords = [
    "bird", "parrot", "parakeet", "finch", "hen", "cock", "sparrow",
    "eagle", "owl", "duck", "goose", "swan"
]

# Función simple para inferir especie
def inferir_especie(texto_labels):
    if any(pal in texto_labels for pal in gato_keywords):
        return "gato"
    if any(pal in texto_labels for pal in perro_keywords):
        return "perro"
    if any(pal in texto_labels for pal in ave_keywords):
        return "ave"
    return "desconocida / no clara"

especie = inferir_especie(labels_text)

resultado = {
    "label_principal": predicciones[0]["label"],
    "score_principal": float(predicciones[0]["score"]),
    "especie_inferida": especie,
    "predicciones_completas": predicciones
}

print(json.dumps(resultado, indent=4, ensure_ascii=False))
