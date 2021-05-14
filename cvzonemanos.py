import cv2
import cvzone # toca usar la version 3.7.8 de python, la 3.9 no funciona, necesita el modulo pip install Serial

cap= cv2.VideoCapture(0) # 0 para la camara del PC
detector= cvzone.HandDetector(maxHands=2,detectionCon=0.7)
#serialPort=cvzone.SerialObject("COM3",9600,1) # parainviar un dato por puerto serial
while(True):
    exito,imagen= cap.read()
    imagen= detector.findHands(imagen)
    listaDedos,bbox= detector.findPosition(imagen) 
    if listaDedos:
        dedos=detector.fingersUp()
        print(dedos)
        #serialPort.sendData(dedos)
    cv2.imshow("ImagenMano", imagen)
    cv2.waitKey(1)