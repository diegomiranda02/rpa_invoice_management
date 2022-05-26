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

# Wait the user input the document number
documentNumber = input("Digite o numero do CPF/CNPJ/Matricula: ")
print("Voce digitou " + documentNumber)

documentNumberConfirm = input("O numero esta correto? Sim ou Nao? ")

if documentNumberConfirm[0] == 'S':
    print("Numero do documento informado com sucesso :" + documentNumber)
elif documentNumberConfirm[0] == 'N':
    print("Programa finalizado.")
    exit()

# Wait the user input the password
password = input("Digite a senha: ")
print("Voce digitou " + password)

passwordConfirm = input("A senha esta correta? Sim ou Nao? ")

if passwordConfirm[0] == 'S':
    print("Senha informado com sucesso :" + password)
elif passwordConfirm[0] == 'N':
    print("Programa finalizado.")
    exit()

# Return to the website to inform the document number
pyautogui.keyDown('alt')
pyautogui.press('tab', presses = 2)
pyautogui.keyUp('alt')

# Type the document number
pyautogui.write(documentNumber)

# Go to the password field
pyautogui.press("tab")

# Type the password
pyautogui.write(password)

