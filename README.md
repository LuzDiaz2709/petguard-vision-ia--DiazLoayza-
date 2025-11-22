# petguard-vision-ia--DiazLoayza-
Proyecto de visión artificial con modelos de Hugging Face para identificar especie animal, generar descripción de imagen, detectar texto y extraer colores dominantes. Incluye scripts en Python ejecutados en Spyder y estructura profesional de carpetas.

# 🐶 PetGuard Visión IA – Análisis de Imágenes con Hugging Face

Este proyecto implementa un sistema de visión artificial aplicado al campo veterinario.  
A partir de una imagen de una mascota, el sistema realiza **cuatro análisis automáticos e independientes**, cada uno ejecutado en un script distinto:

1. Identificación de la **especie del animal**.  
2. Generación de una **descripción automática de la imagen**.  
3. Detección de **texto dentro de la imagen** (OCR).  
4. Obtención de los **colores dominantes**, con nombres de color interpretables por humanos.

Los modelos utilizados provienen de Hugging Face y fueron ejecutados en un entorno limpio configurado en Anaconda y Spyder.

---

## 🎯 **Objetivo del proyecto**

El objetivo principal es aplicar técnicas de inteligencia artificial para analizar imágenes con fines veterinarios, demostrando el uso real de:

- Modelos preentrenados de **Hugging Face**.  
- Procesamiento de imágenes con **Pillow** y **NumPy**.  
- Exportación de resultados estructurados en formato JSON.  
- Scripts modulares para análisis independiente: especie, descripción, texto y color.  

El proyecto simula cómo una clínica veterinaria podría integrar IA para interpretar imágenes de mascotas de manera automática y eficiente.

---

## 🚀 **Instrucciones de ejecución**

### 1. Crear y activar el entorno
Ejecutar en **Anaconda Prompt**:

```bash
conda create -n huggingface python=3.10
conda activate huggingface

2. Instalar dependencias

Desde el entorno activado:

pip install -r requirements.txt

3. Ejecutar cada script por separado

Dentro de la carpeta del proyecto:

python src/especie_animal.py
python src/descripcion_imagen.py
python src/texto_detectado.py
python src/colores_dominantes.py


Cada script generará un archivo JSON en:

assets/resultados/


Los archivos generados son:

resultado_especie.json

resultado_descripcion.json

resultado_texto.json

resultado_colores.json

📦 Dependencias y versiones recomendadas

Este proyecto fue probado con las siguientes librerías:

Librería	Versión recomendada
Python	3.10
transformers	4.x
torch	2.x (CPU)
torchvision	0.x
torchaudio	0.x
pillow	10.x
numpy	1.26
regex	2023.x

Archivo de instalación automática:

requirements.txt
