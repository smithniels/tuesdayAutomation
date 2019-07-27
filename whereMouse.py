# -*- coding: utf-8 -*-
"""
When run, this script finds the x,y cordinates of the mouse on the screen,
and returns the output every second. Press Ctrl+C to hop out of the program.
@author: NSmith
"""


import time, pyautogui

print('Press Ctrl-C to quit.')
x = 4
search = 'freeze 1 row'
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr),\n
		 end='', flush=True)
        time.sleep(1)
        
        x -= 1

except KeyboardInterrupt:
    print('\n')
    
