import time
from automaticmachine import Screen
screen = Screen()


while True:

    screen.effect("---" * 10)
    screen.effect("Welcome to the automatic machine")
    screen.effect("---" * 10)
    screen.effect("Please choose type of bill")
    screen.effect("---" * 10)
    # print("Please choose type of bill")
    time.sleep(1)
    screen.effect("1. 20")
    screen.effect("2. 50")
    screen.effect("3. 100")
    screen.effect("4. 𝑬𝑋𝐼𝘛")
    time.sleep(1)
    screen.effect("___" * 10)
    time.sleep(1)
    option = input('Please select your option : ')
    screen.effect("___" * 10)
    if option == "1":
        if screen.coin_(bank=20):
            break
    elif option == "2":
        if screen.coin_(bank=50):
            break
    elif option == "3":
        if screen.coin_(bank=100):
            break
    elif option == "4":
        break
    else:
        print("Please insert again")

