import numpy
import cv2
import sys
import os
import time
from progress.bar import ChargingBar

file = open('8x8.manus', 'a')

totframes = len(os.listdir('frames/'))

curframe = 1
display = ''

bar = ChargingBar('      Converting fuckframes ', max=totframes)

while True:
    img = cv2.imread('frames/frame'+str(curframe)+'.jpg')
    for i in range(8):
        for j in range(8):
            if(img[i*45][j*60][1]>200):
                display += '1'
            else:
                display += '0'
        display += '\n'
    
    file.write(display)
    display = ''
    #os.system('cls')
    bar.next()
    curframe+=1

file.close()