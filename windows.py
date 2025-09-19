import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('q') == False:
    if pyautogui.pixelMatchesColor(3106, 891, (67, 150, 42)):  # cor verde
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(3191, 896, (234, 51, 35)):  # cor vermelha
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(3283, 892, (244, 244, 81)):
        pyautogui.press('j')
        sleep(0.05)
