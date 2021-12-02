import numpy
import cv2
import sys
import os
import time
import pyautogui as pag

# 480x360

curframe = 1
lastw = True

time.sleep(2)

while True:
    img = cv2.imread('frame'+str(curframe+20)+'.jpg')
    
    print("Currently drawing frame:", curframe)

    for i in range(480):
        
        for j in range(360):
            
            if(img[j][i][1]<100 and lastw==True):
                pag.moveTo(j,i)
                pag.click()
                lastw = False

            elif(img[j][i][1]>100 and lastw==False):
                lastw = True

            
            
    
    #os.system('cls')
    curframe+=1

