from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# Load a model
#modeloEntenado = "runs/detect/train5/weights/best.pt"
modeloEntrenado = "best.pt"
model = YOLO(modeloEntrenado)

#metrics = model.val()  # evaluate model performance on the validation set

#result = model.predict(source="0")
#result = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments
#imgPredict="https://res.cloudinary.com/dgvsnqsq0/image/upload/v1692754492/3546188763956374011502990.jpg"
imgPredict="https://res.cloudinary.com/dgvsnqsq0/image/upload/v1696635573/oxdjzqbqwbm8mijbldxw.png"
#im1 = Image.open(imgPredict)
results = model(source=imgPredict, stream=False)  # save plotted images  # predict on an image



detecciones=[]


for result in results:
    print(result.names)
    
    cv2.imshow("result",  result.plot(conf=True))
    cv2.waitKey(0)
    #print(deteccion.prueba)
    #deteccion.imgResult=result.plot(conf=False)
    boxes = result.boxes
    

    for box in boxes:

        xyxy=[float(box.xyxy[0][0]), float(box.xyxy[0][1]), float(box.xyxy[0][2]), float(box.xyxy[0][3])]
        anchoDeteccion=float(box.xywh[0][2])
        altoDeteccion=float(box.xywh[0][3])

        #deteccion=Deteccion(result.plot(conf=False), "prueba")
        #print(box.xyxy)
        #print(box.xywh)
        print(int(box.cls[0]))
    #print(result.plot(conf=False))

##MUESTRO RECORTES


#print(float(box.xyxy[0][0]))

xinicial=int(box.xyxy[0][0])
yinicial=int(box.xyxy[0][1])
xfinal=int(box.xyxy[0][2])
yfinal=int(box.xyxy[0][3])



#image = cv2.imread('datasets/predictions/dfh10 (72).jpg')

#imageOut = image[xinicial:xfinal,yinicial:yfinal]

#cv2.imshow('Imagen de entrada',image)
#cv2.imshow('Imagen de salida',imageOut)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#res_plotted = result[0].plot(conf=False)
#cv2.imshow("result", res_plotted)
#cv2.waitKey(0)




