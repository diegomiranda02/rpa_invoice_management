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
pyautogui.press("enter")

pyautogui.PAUSE = 3

# Go to Directa Website - https://directa.natal.rn.gov.br/
pyautogui.write("https://directa.natal.rn.gov.br/")
pyautogui.press("enter")

pyautogui.PAUSE = 3

# Go to the login text field
pyautogui.press("tab", presses = 21)


# Return to the terminal to capture the document number
pyautogui.keyDown('alt')
pyautogui.press('tab', presses = 2)
pyautogui.keyUp('alt')
