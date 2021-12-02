import time
import os

file = open('script.manus','r')

frame = 1
line = 1

display = ''

while True:
    for x in range(72):
        display += (file.readline())
    print(display, flush=True)
    time.sleep(1)
