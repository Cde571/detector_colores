import cv2
import numpy as np


imagen = cv2.imread('C:\\Users\\caco2\\Desktop\\limon.png')
imagen = cv2.resize(imagen, (300, 300))
imghsv= cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

amarillobajo= np.array([20,50,50],np.uint8)
amarilloalto= np.array([32,255,255],np.uint8)
mascara1=cv2.inRange(imghsv,amarillobajo,amarilloalto)

verdebajo= np.array([36,50,50],np.uint8)
verdealto =np.array([75,255,255],np.uint8)
mascara2  = cv2.inRange(imghsv,verdebajo,verdealto)

contornoamarillo= cv2.findContours(mascara1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contornoverde= cv2.findContours(mascara2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contornoamarillo[0]:

    if len(c) > 0:
        area= cv2.contourArea(c)
        if area>1000:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,255),2)

for c in contornoverde[0]:

    if len(c) > 0:
        area= cv2.contourArea(c)
        if (area>1000):
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen HSV',imghsv)
cv2.imshow('Inrange amarillo',mascara1)
cv2.imshow('Inrange verde',mascara2)

cv2.waitKey(0)
cv2.destroyAllWindows()
