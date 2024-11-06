import os
import sys
import subprocess
import shutil
import zipfile
from utils import validate_library, ensure_layers_directory

# Obtener la ruta del directorio raíz del proyecto (lambda-layers)
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_layer_zip(library_name, python_version):
    # Validar el nombre de la librería
    validate_library(library_name)
    
    # Asegurar que el directorio 'layers' exista
    layers_dir = os.path.join(project_root, "layers")
    if not os.path.exists(layers_dir):
        os.makedirs(layers_dir)
        print(f"Directorio {layers_dir} creado.")
    
    # Definir rutas absolutas basadas en el directorio raíz del proyecto
    temp_dir = os.path.join(project_root, "temp_layer")
    base_dir = os.path.join(temp_dir, library_name)
    lib_dir = os.path.join(base_dir, "python", "lib", f"python{python_version}", "site-packages")
    bin_dir = os.path.join(base_dir, "bin")
    zip_path = os.path.join(layers_dir, f"{library_name}_layer.zip")

    # Crear los directorios necesarios
    os.makedirs(lib_dir, exist_ok=True)
    os.makedirs(bin_dir, exist_ok=True)

    # Establecer la variable de entorno PIP_USER para evitar el conflicto
    env = os.environ.copy()
    env["PIP_USER"] = "0"

    # Instalar la librería en el directorio temporal
    subprocess.run([sys.executable, "-m", "pip", "install", library_name, "-t", lib_dir], env=env)

    # Crear el archivo .zip
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Obtener el path relativo para mantener la estructura correcta en el zip
                arcname = os.path.relpath(file_path, start=base_dir)
                zipf.write(file_path, arcname)

    # Limpiar el directorio temporal
    shutil.rmtree(temp_dir)
    print(f"Directorio temporal '{temp_dir}' eliminado.")
    print(f"Archivo .zip creado en: {zip_path}")


# Ejemplo de uso
if __name__ == "__main__":
    library_name = "requests"
    python_version = "3.10" 
    # Solicitar al usuario el nombre de la librería y la versión de Python
    #library_name = input("Ingrese el nombre de la librería a empaquetar: ").strip()
    #python_version = input("Ingrese la versión de Python (ejemplo: '3.10'): ").strip()
    create_layer_zip(library_name, python_version)
