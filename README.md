# Pruebas de Búsqueda en Google con Playwright y Python

Este proyecto utiliza Playwright para automatizar una búsqueda en Google.

## Requisitos

- Python 3.7 o superior
- Playwright

## Instalación

### Paso 1: Descomprimir el archivo.

### Paso 2: Instalar Python
Para instalar Python, descargar: https://www.python.org/downloads/

Recuerda cual es el alias de la instalación de Python, dependiendo puede ser **python** o **python3**.


### Paso 3: Crear un entonrno virtual
Una vez Python instalado, ejecuta: 
> **python3** -m venv env   
> source env/bin/activate # En Windows usa `env\Scripts\activate` 

### Paso 4: Instalar los Playwright
> pip install -r requirements.txt

### Paso 5: Instalar los navegadores de Playwright
> **python3** -m playwright install

# Ejecución de las Pruebas

### Paso 1: Ejecutar el script de pruebas

> **python3** test_website.py