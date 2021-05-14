import mediapipe as mp
import cv2
import time     
ctime=0
ptime=0
# cargar el modelo de mediapipe
mpose=mp.solutions.pose
poses= mpose.Pose()
mpdraw= mp.solutions.drawing_utils


cap= cv2.VideoCapture(0)

while(True):
    exito, imagen= cap.read()
    imagenRGB= cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    resultado= poses.process(imagen)
    #print(resultado.pose_landmarks)
    lmlist=[]
    if resultado.pose_landmarks:
        # para ver los puntos y las lineas, ID son los puntos landmarks
        mpdraw.draw_landmarks(imagen,resultado.pose_landmarks,mpose.POSE_CONNECTIONS)
        for ID,lm in  enumerate(resultado.pose_landmarks.landmark):
            h,w,ch = imagen.shape
            #print(ID ,lm)
            # para imprimirlos punto de marca landmarks en pixels
            cx, cy = int(lm.x*w),int(lm.y*h)
            lmlist.append([ID,cx,cy])
        if len(lmlist)!=0:
            #print(lmlist)
            # marca de color azul el punto que se desee. 11 es el hombro izq, 15 y 16 las muñecas
            cv2.circle(imagen,(lmlist[15][1],lmlist[15][2]),10,(255,0,0),cv2.FILLED)
            cv2.circle(imagen,(lmlist[16][1],lmlist[16][2]),10,(255,0,0),cv2.FILLED)
    # para ver los FPS
    ctime=time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(imagen,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
 
    cv2.imshow("Imagen", imagen)
    cv2.waitKey(1)

