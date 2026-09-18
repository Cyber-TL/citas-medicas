# src/gestion_datos.py
import json
import os


def cargar_citas(ruta_archivo: str) -> list:
    if not os.path.exists(ruta_archivo):
        return []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_citas(ruta_archivo: str, datos: list) -> bool:
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        return True
    except Exception as error:
        print(f"Error al guardar los datos: {error}")
        return False