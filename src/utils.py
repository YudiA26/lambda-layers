# src/utils.py
import os

def validate_library(library_name):
    """Verifica que el nombre de la librería sea válido."""
    if not library_name:
        raise ValueError("El nombre de la librería no puede estar vacío.")
    print(f"Librería '{library_name}' validada.")

def ensure_layers_directory():
    """Crea el directorio 'layers' si no existe."""
    layers_dir = "../layers"
    if not os.path.exists(layers_dir):
        os.makedirs(layers_dir)
        print(f"Directorio {layers_dir} creado.")
    else:
        print(f"Directorio {layers_dir} ya existe.")
