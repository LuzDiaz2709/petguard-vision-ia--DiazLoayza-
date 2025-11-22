from transformers import pipeline  # solo para mantener formato solicitado
from PIL import Image
import json
import numpy as np
import colorsys

# --- Función para clasificar un pixel en un nombre de color humano ---
def nombre_color_humano(r, g, b):
    # Normalizar a [0,1] para HSV
    rn, gn, bn = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(rn, gn, bn)  # h en [0,1]
    h_deg = h * 360  # pasamos a grados para entender mejor

    # Primero, casos de blanco / gris / negro (baja saturación)
    if v < 0.15:
        return "negro"
    if s < 0.15:
        if v > 0.85:
            return "blanco"
        elif v > 0.4:
            return "gris"
        else:
            return "gris oscuro"

    # Ahora analizamos por tono (hue)
    # Rojos / rosas / fucsias
    if (h_deg >= 345 or h_deg < 15):
        return "rojo"
    if 315 <= h_deg < 345:
        return "fucsia"
    if 290 <= h_deg < 315:
        return "rosado"

    # Naranjas / marrones
    if 15 <= h_deg < 40:
        # Si está algo oscuro → marrón / marrón oscuro
        if v < 0.45:
            return "marrón oscuro"
        elif v < 0.75:
            return "marrón"
        else:
            return "marrón claro"

    # Amarillos / beige / crema
    if 40 <= h_deg < 65:
        if v > 0.85:
            return "crema"
        else:
            return "beige"

    # Verdes
    if 65 <= h_deg < 150:
        if v > 0.7 and s > 0.5:
            return "verde césped"
        elif v < 0.4:
            return "verde oscuro"
        else:
            return "verde"

    # Cianes / turquesas
    if 150 <= h_deg < 190:
        return "turquesa"

    # Azules
    if 190 <= h_deg < 255:
        if v < 0.4:
            return "azul oscuro"
        else:
            return "azul"

    # Violetas / púrpuras
    if 255 <= h_deg < 290:
        return "morado"

    # Por si algo se escapa:
    return "otros"

# --- 1. Cargar imagen ---
imagen = Image.open("perro2.jpg").convert("RGB")

# --- 2. Reducir tamaño para que el cálculo sea manejable ---
img_peq = imagen.resize((128, 128))
arr = np.array(img_peq)  # shape (128,128,3)
total_pixeles = arr.shape[0] * arr.shape[1]

# --- 3. Recorrer pixeles y agrupar por nombre de color ---
agrupados = {}  # nombre -> {count, sum_r, sum_g, sum_b}

for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
        r, g, b = arr[y, x]
        nombre = nombre_color_humano(int(r), int(g), int(b))

        if nombre not in agrupados:
            agrupados[nombre] = {
                "count": 0,
                "sum_r": 0,
                "sum_g": 0,
                "sum_b": 0
            }

        agrupados[nombre]["count"] += 1
        agrupados[nombre]["sum_r"] += int(r)
        agrupados[nombre]["sum_g"] += int(g)
        agrupados[nombre]["sum_b"] += int(b)

# --- 4. Construir lista con promedio RGB y porcentaje por color ---
lista_colores = []

for nombre, data in agrupados.items():
    count = data["count"]
    prom_r = round(data["sum_r"] / count)
    prom_g = round(data["sum_g"] / count)
    prom_b = round(data["sum_b"] / count)
    porcentaje = round((count / total_pixeles) * 100, 2)

    hex_code = "#{:02x}{:02x}{:02x}".format(prom_r, prom_g, prom_b)

    lista_colores.append({
        "nombre_color": nombre,
        "rgb_promedio": {
            "r": prom_r,
            "g": prom_g,
            "b": prom_b
        },
        "hex_promedio": hex_code,
        "porcentaje_aproximado": porcentaje
    })

# --- 5. Ordenar por porcentaje de mayor a menor ---
lista_colores_ordenada = sorted(
    lista_colores,
    key=lambda x: x["porcentaje_aproximado"],
    reverse=True
)

# Puedes limitar a los 6 colores más dominantes
colores_dominantes = lista_colores_ordenada[:6]

# --- 6. JSON final ---
resultado = {
    "colores_dominantes": colores_dominantes
}

print(json.dumps(resultado, indent=4, ensure_ascii=False))

