import pyautogui 
import time  

def SendMessage():
    time.sleep(2) 
    message = "Spam"
    iterations = 200

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1
 
        pyautogui.typewrite(message.strip()) 
        pyautogui.press('enter') 
    print("Вся обойма попала в нашу жертву!")

print("Запуск сделан, осталось заспамить жертву! ^_^")
print('~'*1)
print("[1]==>Спам Жертвы!)")
print('~'*1)
option = input("[Выбирай функцию]===> ")

if option == "1":
    SendMessage()
else:
    print('Выбирай функцию 1 !!!')
