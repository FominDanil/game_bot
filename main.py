from time import sleep
import cv2
from mss import mss
import numpy as np
import pyautogui
monr = {
    'top': 586,
    'left': 941,
    'width': 35,
    'height': 80
}
monl = {
    'top': 586,
    'left': 820,
    'width': 41,
    'height': 70
}
slt = 0.05
# {'left': 0, 'top': 0, 'width': 1512, 'height': 982}
sleep(5)
side = 0
with mss() as sct:
    for i in range(500):

        imgl = np.asarray(sct.grab(monl))
        imgr = np.asarray(sct.grab(monr))
        # create hsv
        hsvl = cv2.cvtColor(imgl, cv2.COLOR_BGR2HSV)
        hsvr = cv2.cvtColor(imgr, cv2.COLOR_BGR2HSV)

        lower_red = np.array([12, 166, 157])
        upper_red = np.array([13, 171, 159])
        maskl = cv2.inRange(hsvl, lower_red, upper_red)
        maskr = cv2.inRange(hsvr, lower_red, upper_red)

        # print(type(mask0))
        if side:
            if maskr.any():
                pyautogui.click(x=700, y=500)
                sleep(slt)
                pyautogui.click(x=700, y=500)
                side = 0
            else:
                pyautogui.click(x=1000, y=500)
        else:
            if maskl.any():
                pyautogui.click(x=1000, y=500)
                sleep(slt)
                pyautogui.click(x=1000, y=500)
                side = 1
            else:
                pyautogui.click(x=700, y=500)

        sleep(slt)




