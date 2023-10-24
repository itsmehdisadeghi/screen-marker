import cv2
import numpy as np


mypointtt = []
def drawpoint(mypoint):
    for poi in mypoint:
        cv2.circle(imagee , (poi[0],poi[1]) , 10 , (255,0 , 0) , cv2.FILLED)
        
def getcontour(img):
    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imag , cnt , -1 , (0,255,255) , 4)
            per = cv2.arcLength(cnt , True)
            approx = cv2.approxPolyDP(cnt , 0.02*per , True)
            x , y , w , h = cv2.boundingRect(approx)    
            cv2.circle(imagee , (x,y) , 10 , (255,0 , 0) , cv2.FILLED)
            mypointtt.append([x,y])
cap = cv2.VideoCapture(0)
cap.set(10 , 1)

while True:
    suc , img = cap.read()
    img = cv2.resize(img , (1600 , 800))
    img = cv2.flip(img, 1)
    imagee = img.copy()
    hsvimg = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower  = np.array([101 , 116 , 78])
    upper  = np.array([118 , 255 , 255])
    mask = cv2.inRange(hsvimg , lower , upper)  
    imgr = cv2.bitwise_and(img , img , mask=mask)
    imag = img.copy()
    getcontour(mask)
    drawpoint(mypointtt)
    # cv2.imshow("maskimage"  , mask)
    # cv2.imshow("result"  , imgr)
    # cv2.imshow("resulft"  , imag)
    cv2.imshow("resul"  , imagee)
    if cv2.waitKey(1) & 0xFF ==ord(' '):
         cv2.destroyAllWindows()
         break