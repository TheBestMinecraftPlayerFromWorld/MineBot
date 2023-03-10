from pynput.keyboard import Key, Listener
from time import sleep as wait
# Python program to take
# screenshots
import os

wait(10)
if not os.path.exists("data"):
    os.mkdir("data")
print("GOGO")

pressed_keys = set()

def on_press(key):
    if key == Key.esc:
        print("Bye!")
        exit()
    pressed_keys.add(key)
    print("Pressed:", ", ".join(str(k) for k in pressed_keys))
    x()
def on_release(key):
    pressed_keys.discard(key)
def x():
    #while not keyboard.pressed(Key.esc):
    if not len(pressed_keys) == 0:
        import numpy as np
        import cv2
        import pyautogui


        # take screenshot using pyautogui
        image = pyautogui.screenshot()

        # since the pyautogui takes as a
        # PIL(pillow) and in RGB we need to
        # convert it to numpy array and BGR
        # so we can write it to the disk
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)

        # writing it to the disk using opencv
        
        for x in pressed_keys:
            k = os.path.join("data",str(x).replace("'",""))
            if not os.path.exists(k):
                os.mkdir(k)
            l = len(os.listdir(k))
            cv2.imwrite(os.path.join(k,f"img_{l}.png"), image)
def lstnr():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
lstnr()
