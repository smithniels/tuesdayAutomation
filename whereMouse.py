# -*- coding: utf-8 -*-
"""

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
    