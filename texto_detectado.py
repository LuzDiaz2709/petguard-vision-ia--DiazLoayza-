from transformers import pipeline
from PIL import Image
import json
import re

# 1. Modelo OCR (igual que antes)
detector = pipeline(
    "image-to-text",
    model="microsoft/trocr-base-printed"
)

# 2. Cargar la imagen
imagen = Image.open("perro2.jpg").convert("RGB")

# 3. Pasar la imagen al modelo
salida = detector(imagen)

# 4. Extraer el texto bruto devuelto por el modelo
if len(salida) > 0 and "generated_text" in salida[0]:
    texto_bruto = salida[0]["generated_text"].strip()
else:
    texto_bruto = ""

# 5. Heurística para decidir si es texto "real" o solo ruido
#    - Eliminamos caracteres raros
#    - Vemos si hay letras
#    - Vemos si tiene una longitud mínima

def limpiar_texto(t):
    # quitar espacios y símbolos raros
    return re.sub(r"[^A-Za-z0-9áéíóúÁÉÍÓÚñÑ]", "", t)

texto_limpio = limpiar_texto(texto_bruto)

tiene_letras = any(c.isalpha() for c in texto_limpio)
suficiente_longitud = len(texto_limpio) >= 4  # puedes ajustar este umbral

if tiene_letras and suficiente_longitud:
    # Aceptamos que probablemente hay texto
    hay_texto = True
    texto_detectado = texto_bruto
    porcentaje_probable_texto = 100
else:
    # Consideramos que NO hay texto relevante
    hay_texto = False
    texto_detectado = ""
    porcentaje_probable_texto = 0

# 6. Armar el JSON de resultado
resultado = {
    "hay_texto": hay_texto,
    "porcentaje_probable_texto": porcentaje_probable_texto,
    "texto_detectado": texto_detectado,
    "texto_bruto_modelo": texto_bruto,
    "salida_cruda_modelo": salida
}

# 7. Imprimir el JSON bonito en consola
print(json.dumps(resultado, indent=4, ensure_ascii=False))

