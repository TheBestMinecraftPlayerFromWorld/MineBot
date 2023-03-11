from pynput.keyboard import Key, Listener
from time import sleep as wait
from pynput import mouse
import keyboard
import pynput
# Python program to take
# screenshots
import os

wait(3)
if not os.path.exists("data"):
    os.mkdir("data")
print("GOGO")

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    
    print("Pressed:", ", ".join(str(k) for k in pressed_keys))
    x()
def on_release(key):
    pressed_keys.discard(key)
import numpy as np
import cv2
import pyautogui
def x():
    image = takeScreenshot()
    if (pynput.keyboard.KeyCode(char="w") in pressed_keys or pynput.keyboard.KeyCode(char="\x17") in pressed_keys) and Key.ctrl_l in pressed_keys:
        writeToImg("WS",image)
    elif pynput.keyboard.KeyCode(char="w") in pressed_keys:
        writeToImg("W",image)
    elif pynput.keyboard.KeyCode(char="a") in pressed_keys:
        writeToImg("A",image)
    elif pynput.keyboard.KeyCode(char="s") in pressed_keys:
        writeToImg("S",image)
    elif pynput.keyboard.KeyCode(char="d") in pressed_keys:
        writeToImg("D",image)
    elif pynput.keyboard.KeyCode(char="e") in pressed_keys:
        writeToImg("E",image)
    elif Key.esc in pressed_keys:
        writeToImg("ESC",image)
    elif Key.space in pressed_keys:
        writeToImg("JUMP",image)
def takeScreenshot():
    #while not keyboard.pressed(Key.esc):
    # take screenshot using pyautogui
    image = pyautogui.screenshot()

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)

    # writing it to the disk using opencv
    return image
    """for x in pressed_keys:
        k = os.path.join("data",str(x).replace("'",""))
        if not os.path.exists(k):
            os.mkdir(k)
        l = len(os.listdir(k))
        cv2.imwrite(os.path.join(k,f"img_{l}.png"), image)"""
mx = 0
my = 0
def on_move(x1,y1):
    global mx,my
    print(x1,y1) 
    mx+=x1
    my+=y1
def on_click(x, y, button, pressed):
    print(button)
    image = takeScreenshot()
    if button == mouse.Button.left:
        writeToImg(f"mL{pressed}",image)
    if button == mouse.Button.middle:
        writeToImg(f"mM{pressed}",image)
    if button == mouse.Button.right:
        writeToImg(f"mR{pressed}",image)
def writeToImg(name,image):
    k = os.path.join("data",name)
    if not os.path.exists(k):
        os.mkdir(k)
    l = len(os.listdir(k))
    cv2.imwrite(os.path.join(k,f"img_{l}.png"), image)
import threading
def lstnr():
    global x2,x11
    thread = threading.Thread(target=sThread)
    thread.start()
    with mouse.Listener(on_click=on_click) as listener:
        x11 = listener
        x2 = None
        with Listener(on_press=on_press,on_release=on_release) as listener:
            x2 = listener
            x2.join()
            x11.join()
    thread.join()
    #x2.join()
    print("BYE")

def sThread():
    
    while not Key.backspace in pressed_keys:
        s = pyautogui.position()
        wait(0.5)
        mx = pyautogui.position().x-s.x
        my = pyautogui.position().y-s.y
        # take screenshot using pyautogui
        image = pyautogui.screenshot()

        # since the pyautogui takes as a
        # PIL(pillow) and in RGB we need to
        # convert it to numpy array and BGR
        # so we can write it to the disk
        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)
        print(mx,my)
        if mx > 0:
            writeToImg("mx+",image)
        if my > 0:
            writeToImg("my+",image)
        if mx < 0:
            writeToImg("mx-",image)
        if my < 0:
            writeToImg("my-",image)
        mx = 0
        my = 0
    x2.stop()
    x11.stop()
lstnr()
