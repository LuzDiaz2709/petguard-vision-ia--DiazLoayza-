# petguard-vision-ia--DiazLoayza-
Proyecto de visión artificial con modelos de Hugging Face para identificar especie animal, generar descripción de imagen, detectar texto y extraer colores dominantes. Incluye scripts en Python ejecutados en Spyder y estructura profesional de carpetas.

# 🐶 PetGuard Visión IA – Análisis de Imágenes con Hugging Face

Este proyecto implementa un sistema de visión artificial aplicado al campo veterinario.  
A partir de una imagen de una mascota, el sistema realiza **cuatro análisis automáticos**, cada uno ejecutado en un script independiente:

1. Identificación de la **especie del animal**  
2. Generación de una **descripción automática de la imagen**  
3. Detección de **texto dentro de la imagen** (OCR)  
4. Obtención de los **colores dominantes** con nombres interpretables por humanos  

Los modelos utilizados provienen de Hugging Face y fueron ejecutados usando Spyder en un entorno limpio configurado en Anaconda.

---

## 🎯 OBJETIVO DEL PROYECTO

El objetivo de este proyecto es aplicar inteligencia artificial al análisis de imágenes veterinarias, integrando modelos de visión preentrenados para:

- Evaluar y clasificar contenido visual  
- Generar descripciones automáticas  
- Detectar texto relevante  
- Reconocer los colores más representativos de la imagen  
- Exportar resultados como JSON estructurado  

Este enfoque permite simular cómo una clínica veterinaria podría automatizar el análisis básico de imágenes enviadas por dueños de mascotas.

---

## 🚀 INSTRUCCIONES DE EJECUCIÓN

### 1️⃣ Crear el entorno de trabajo en Anaconda

Ejecutar en **Anaconda Prompt**:

```bash
conda create -n huggingface python=3.10
conda activate huggingface

### 1️⃣ Instalar las dependencias del documento
pip install -r requirements.txt


### 1️⃣ Ejecutar los scripts del analisis
python src/especie_animal.py
python src/descripcion_imagen.py
python src/texto_detectado.py
python src/colores_dominantes.py
assets/resultados/

📦 DEPENDENCIAS Y VERSIONES

Este proyecto fue probado con las siguientes versiones:

Librería	Versión recomendada
Python	3.10
transformers	4.x
torch (CPU)	2.x
torchvision	0.x
torchaudio	0.x
pillow	10.x
numpy	1.26
regex	2023.x

requirements.txt



