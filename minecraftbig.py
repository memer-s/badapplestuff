import numpy
import cv2
import sys
import os
import time
from progress.bar import ChargingBar

file = open('minecraftbig.manus', 'a')

totframes = len(os.listdir('frames/'))

curframe = 1
display = ''

bar = ChargingBar('      Converting fuckframes ', max=totframes)

while True:
    img = cv2.imread('frames/frame'+str(curframe)+'.jpg')
    for i in range(72):
        for j in range(96):
            if(img[i*5][j*5][1]>100):
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
