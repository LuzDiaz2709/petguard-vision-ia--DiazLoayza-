from transformers import pipeline
from PIL import Image
import json

# 1. Cargar el modelo de "image captioning"
#    Este modelo genera una frase describiendo la imagen.
detector = pipeline(
    "image-to-text",
    model="nlpconnect/vit-gpt2-image-captioning"
)

# 2. Abrir la imagen
imagen = Image.open("perro2.jpg").convert("RGB")

# 3. Obtener la descripción generada por el modelo
salida = detector(imagen)

# salida suele ser una lista, tomamos el primer resultado
descripcion = salida[0]["generated_text"]

# 4. Armar el JSON de resultado
resultado = {
    "descripcion_imagen": descripcion,
    "salida_cruda_modelo": salida
}

# 5. Imprimir el JSON bonito en consola
print(json.dumps(resultado, indent=4, ensure_ascii=False))
