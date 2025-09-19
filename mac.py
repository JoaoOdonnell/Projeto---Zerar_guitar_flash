from pynput import keyboard
import pyautogui
from time import sleep

running = True


def on_press(key):
    global running
    try:
        if key.char == '1':
            running = False
            return False
    except:
        pass


listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    # cor verde
    if pyautogui.pixelMatchesColor(1746, 720, (15, 141, 30), tolerance=80):
        pyautogui.press('a')
        sleep(0.02)
    # cor vermelha
    if pyautogui.pixelMatchesColor(1834, 720, (254, 16, 22), tolerance=80):
        pyautogui.press('s')
        sleep(0.02)
    # cor amarela
    if pyautogui.pixelMatchesColor(1923, 720, (243, 242, 65), tolerance=80):
        pyautogui.press('j')
        sleep(0.02)
