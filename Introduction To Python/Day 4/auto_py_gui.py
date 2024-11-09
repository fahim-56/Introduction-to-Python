import pyautogui

str="Fahim Chowdhury!"
pyautogui.write(str, interval=1)

from time import sleep
sleep(5)
for i in range(0,3):
    pyautogui.write("Fahim Chowdhury!", interval=1)
    pyautogui.press('enter')

# jeikhane cursor thakbe oikhane lekha hobe
