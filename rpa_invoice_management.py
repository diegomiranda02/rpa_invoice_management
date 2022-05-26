import pyautogui
import sys

# Point(x=37, y=964) - Position of the Windows Button
pyautogui.moveTo(x=37, y=964)

# Click the Windows Button
pyautogui.click(x=37, y=964, button='left')

pyautogui.PAUSE = 2

# Point(x=834, y=68) - Position of the search bar
pyautogui.moveTo(x=834, y=68)

# Click the search bar
pyautogui.click(x=834, y=68, button='left')

# Type Firefox
pyautogui.write("Firefox", interval=0.25)
