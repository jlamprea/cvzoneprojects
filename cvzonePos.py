import cvzone # toca usar la version 3.7.8 de python, la 3.9 no funciona, necesita el modulo pip install Serial
import cv2

cap= cv2.VideoCapture(0) # 0 para la camara del PC
# no funciona, problema al generar la clase
#detector= cvzone.PoseDetector(mode=True,smooth=False)
fsc= cvzone.FPS()

while(True):
    exito,imagen= cap.read()
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    imagen= cv2.resize(imagen,(640,480))
    #imagenRGB= cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    fsc.update(imagen)
    
    #result=detector.findPosition(imagen)     
    cv2.imshow("ImagenPOS", imagen)
    cv2.waitKey(1)