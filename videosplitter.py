import numpy as np
import cv2
import sys
from progress.bar import ChargingBar



cap = cv2.VideoCapture(sys.argv[1])
arg2 = int(sys.argv[2])

totframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

bar = ChargingBar('      Splitting video... ', max=totframes)

num = 0
nam = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    num += 1
    
    if(arg2>1):
        if(num%arg2==0):
            nam+=1
            cv2.imwrite('frames/frame'+str(nam)+'.jpg', frame)
    else:
        nam+=1
        cv2.imwrite('frames/frame'+str(nam)+'.jpg', frame)
    
    bar.next()
    
    

cap.release()
cv2.destroyAllWindows()