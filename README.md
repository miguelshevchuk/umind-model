# YOLO

El modelo entrenado, esta basado en el modelo YOLO. Utilizamos las librerias de Ultralitycs para podes realizar el entrenamiento y pruebas del modelo


## Estructura

Este proyecto contiene 3 archivos importantes:

**train.py:** Contiene el uso de las librerias de Ultralitycs para realizar el entrenamiento del modelo  
**predict.py:** Contiene el uso de las librerias de Ultralitycs para probar con imagenes en especifico, el rendimiento del modelo  
**yolov8n.pt:** Es el modelo de YOLO que se utiliza de base para nuestro modelo

## Instalacion

### Prerequisitos

Usted necesita tener Python 3 instalado en su PC para poder levantar este proyecto

### Preparacion del ambiente

Se debe generar un espacio virtual de Python para levantar el proyecto. Ejecute los siguientes comandos en la terminal desde la _raiz_ del proyecto
```bash
python -m venv ./venv
. ./venv/bin/activate
```
### Instalacion de dependencias

Para instalar las dependencias del proyecto, ejecute el siguiente comando en la terminal

```bash
pip install -r requirements.txt
```

### Ejecutar entrenamiento

Para iniciar el entrenamiento del modelo, ejecute el siguiente comando en la terminal desde la _raiz_ del proyecto

```bash
python train.py
```

Tenga en cuenta que este proceso consume muchos recursos de la PC, y puede llegar a tardar horas.
En este proyecto, no se incluyen las imagenes etiquetadas por el peso. Se dejaran algunas de ejemplo.

## Pruebas

### Prediccion

Para poder probar un modelo entrenado, se debe copiar el modelo a la carpeta _"./src"_. El modelo se encuentra en la carpeta _"./runs/detect/trainxx/weights/best.pt"_ (Se deja un modelo entrenado de ejemplo).  
Una vez copiado el archivo, ejecutar el siguiente comando desde la carpeta "_./src_"

```bash
python predict.py
```