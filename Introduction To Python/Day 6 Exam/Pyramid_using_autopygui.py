import pyautogui
from time import sleep

N = int(input())

sleep(5)
for i in range(1,N+1):
    for j in range (1,i+1):
        pyautogui.write('#', interval=1)
    pyautogui.press('enter')