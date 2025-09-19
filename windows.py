import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('q') == False:
    if pyautogui.pixelMatchesColor(1258, 713, (67, 150, 42), tolerance=80):  # cor verde
        pyautogui.press('a')
        sleep(0.05)
    # cor vermelha
    if pyautogui.pixelMatchesColor(1346, 712, (234, 51, 35), tolerance=80):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1437, 713, (243, 242, 4), tolerance=50):
        pyautogui.press('j')
        sleep(0.05)
