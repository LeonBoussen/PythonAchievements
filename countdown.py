import os
import time
import webbrowser

t=10
s=0
while t > 0:
    time.sleep(1)
    t -= 1
    print(t)

while t == 0:
    time.sleep(1)
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
    break