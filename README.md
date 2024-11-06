# Lambda Layer Creator

Este proyecto permite crear archivos `.zip` con capas (layers) de AWS Lambda de manera automática. Estas capas contienen las librerías especificadas, organizadas en una estructura compatible con Lambda, y están listas para ser cargadas en AWS como capas reutilizables. Esto es útil para empaquetar librerías que se utilizarán en funciones Lambda sin necesidad de incluirlas en el código de cada función.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:
```
lambda-layer-creator/
├── layers/ # Carpeta donde se almacenarán los archivos `.zip` generados 
├── src/ 
│ ├── create_layer.py # Script principal para crear el archivo .zip 
│ ├── utils.py # Funciones de utilidad (validación de entrada y directorios) 
└── README.md # Este archivo con las instrucciones
```
### Descripción de Archivos y Carpetas

- **`layers/`**: Carpeta de salida donde se guardan los archivos `.zip` generados para las capas de Lambda.
- **`src/`**: Carpeta principal que contiene el código fuente.
  - **`create_layer.py`**: Script principal que ejecuta el proceso de instalación de la librería, crea la estructura compatible con Lambda y genera el archivo `.zip`.
  - **`utils.py`**: Contiene funciones auxiliares para validar la entrada del usuario y asegurar que el directorio `layers` esté creado.
- **`README.md`**: Documento de ayuda y explicación sobre el uso del proyecto.
- **`requirements.txt`**: Archivo opcional donde se pueden agregar dependencias adicionales (en este caso no es necesario, pero puede utilizarse para futuros desarrollos).



## Requisitos

- **Python 3.10 o superior**: Asegúrate de tener Python instalado y accesible desde la línea de comandos.
- **pip**: La herramienta de instalación de paquetes de Python debe estar configurada correctamente.

## Instrucciones de Uso

1. **Clona el repositorio o descarga los archivos** en tu máquina local.
   
2. **Navega a la carpeta `src`** dentro del proyecto en tu terminal:

   ```bash
   cd lambda-layer-creator/src
3. **Navega a la carpeta `src`** dentro del proyecto en tu terminal:

   ```bash
   python create_layer.py
4. **Sigue las instrucciones en pantalla**. Se te pedirá ingresar:
    - **Nombre de la librería** que utilizarás (por ejemplo, `requests`).
    - **Versión de Python** que utilizarás (por ejemplo, `3.10`).
5. **Salida:** El script creará un archivo `.zip` en la carpeta `layers` dentro del proyecto. Este archivo contendrá la librería en la estructura compatible con Lambda, y estará listo para ser cargado como una capa de Lambda en AWS.

6. **Limpieza automática**: Después de crear el archivo `.zip`, el script elimina automáticamente la carpeta temporal temp_layer, por lo que no se quedan archivos residuales.

