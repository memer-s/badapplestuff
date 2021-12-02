import numpy
import cv2
import sys
import os
import time
from progress.bar import ChargingBar

file = open('minecraft.manus', 'a')

totframes = len(os.listdir('frames/'))

curframe = 1
display = ''

bar = ChargingBar('      Converting fuckframes ', max=totframes)

while True:
    img = cv2.imread('frames/frame'+str(curframe)+'.jpg')
    for i in range(36):
        for j in range(48):
            if(img[i*10][j*10][1]>100):
                display += '0'
            else:
                display += '1'

        display += '\n'
    
    file.write(display)
    display = ''
    #os.system('cls')
    bar.next()
    curframe+=1

file.close()
