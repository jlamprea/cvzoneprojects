import cvzone # toca usar la version 3.7.8 de python, la 3.9 no funciona, necesita el modulo pip install Serial
import cv2
import numpy as np

cap= cv2.VideoCapture(0) # 0 para la camara del PC
detector= cvzone.FaceDetector(minDetectionCon=0.5)
fsc= cvzone.FPS()

while(True):
    exito,imagen= cap.read()
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    imagenResize= cv2.resize(imagen,(640,480))
    imagenfsc= fsc.update(imagen)
    #imagenarray= np.asarray_chkfinite(imagenResize)
    listF=detector.findFaces(imagen)
    #print(listF)   
    cv2.imshow("ImagenCara", imagen)
    cv2.waitKey(1)