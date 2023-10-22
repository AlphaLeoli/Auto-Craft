from pynput.keyboard import Key, Listener
import pyautogui
import keyboard
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
tnt_minecart = os.path.join(script_directory, 'tnt_minecart.png')
iron_ingot = os.path.join(script_directory, 'iron_ingot.png')
minecart = os.path.join(script_directory, 'minecart.png')
iron_done = os.path.join(script_directory, 'iron_done.png')
lone_minecart = os.path.join(script_directory, 'lone_minecart.png')

print("Running AutoCraft! Press Insert to auto craft and don't close out of this window until you're done playing :D")

def craftTntMinecart():
    pyautogui.moveTo(200, 200)
    tntMinecartLocation = pyautogui.locateOnScreen(tnt_minecart)
    if tntMinecartLocation is not None:
        x, y = pyautogui.center(tntMinecartLocation)
        for i in range(9):
            pyautogui.click(x, y)

def craftMinecart():
    pyautogui.moveTo(200, 200)
    minecartLocation = pyautogui.locateOnScreen(minecart)
    if minecartLocation is not None:
        keyboard.press('shift')
        pyautogui.sleep(0.1)
        x, y = pyautogui.center(minecartLocation)
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
        keyboard.release('shift')
        craftTntMinecart()

def craftIron():
    ironLocation = pyautogui.locateOnScreen(iron_ingot)
    if ironLocation is not None:
        x, y = pyautogui.center(ironLocation)
        pyautogui.click(x, y)
        pyautogui.moveTo(200, 200)
        for i in range(5):
            pyautogui.click(x, y)
        craftMinecart()

def keyPress(key):
    if key == Key.insert:
        craftIron()

with Listener(on_press=keyPress) as listener:
    listener.join()