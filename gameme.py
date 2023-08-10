import time
import pyautogui
import cv2
import numpy as np
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import random


def movepng(pngfile, confi, waittime=0):
    location1 = pyautogui.locateOnScreen(pngfile[0], confidence=confi)
    location2 = pyautogui.locateOnScreen(pngfile[1], confidence=confi)
    time.sleep(1)
    while location1 is None and location2 is None:
        time.sleep(1)
        location1 = pyautogui.locateOnScreen(pngfile[0], confidence=confi)
        location2 = pyautogui.locateOnScreen(pngfile[1], confidence=confi)

    if location1:
        location = location1
    if location2:
        location = location2
    print(location)
    location_center = pyautogui.center(location)
    pyautogui.moveTo(location)
    pyautogui.mouseDown()
    pyautogui.moveTo(random.randint(1300, 1500), random.randint(520, 560), duration=random.uniform(0.5, 1))
    pyautogui.mouseUp()
    time.sleep(waittime)
    return True


def clickpng(pngfile, confi, waittime):
    location = pyautogui.locateOnScreen(pngfile, confidence=confi)
    while location is None:
        time.sleep(1)
        location = pyautogui.locateOnScreen(pngfile, confidence=confi)

    print(location)
    location_center = pyautogui.center(location)
    pyautogui.click(location_center)
    time.sleep(waittime)
    return True


def doubleclickpng(pngfile, confi, waittime):
    location = pyautogui.locateOnScreen(pngfile, confidence=confi)
    while location is None:
        time.sleep(1)
        location = pyautogui.locateOnScreen(pngfile, confidence=confi)

    print(location)
    location_center = pyautogui.center(location)
    pyautogui.doubleClick(location_center)
    time.sleep(waittime)
    return True


def clickchuansong(pngfile):
    task_location = pyautogui.locateOnScreen(pngfile, confidence=0.98)
    print(task_location)
    # 计算传送按钮的位置
    transfer_button_x = task_location.left + task_location.width // 2
    transfer_button_y = task_location.top + task_location.height * 0.9
        # 点击传送按钮
    pyautogui.click(transfer_button_x, transfer_button_y)
    time.sleep(2)


def replay_events(filename):
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()

    with open(filename, 'r') as file:
        events = file.read().splitlines()

    for event in events:
        event_parts = event.split()
        event_type = event_parts[0]

        if event_type == 'click':
            if len(event_parts) >= 5:
                _, x, y, button, pressed = event_parts
                x, y = int(x), int(y)
                pressed = (pressed == 'True')
                mouse_controller.position = (x, y)
                if button == 'Button.left':
                    if pressed:
                        mouse_controller.press(Button.left)
                    else:
                        mouse_controller.release(Button.left)
                elif button == 'Button.right':
                    if pressed:
                        mouse_controller.press(Button.right)
                    else:
                        mouse_controller.release(Button.right)
        elif event_type == 'press':
            if len(event_parts) >= 1:
                _, key_name = event_parts
                if key_name == 'Key.enter':
                    keyboard_controller.press(Key.enter)
                    keyboard_controller.release(Key.enter)
                else:
                    keyboard_controller.press(key_name)
        elif event_type == 'interval':
            if len(event_parts) >= 1:
                _, interval = event_parts
                time.sleep(float(interval))