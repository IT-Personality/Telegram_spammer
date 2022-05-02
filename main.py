import pyautogui
import time

print("Запуск сделан!")

def SendMessage():
    message = input("Введите сообщение:")
    amount = 30
    time.sleep(6)

    for i in range(amount):
        pass

    while amount > 0:
        amount -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')

SendMessage()