import json
import random
import subprocess
import time
import sys

class OpenFile:
    def __init__(self):
        with open('machine.json', "r") as machine:
            self.machine = json.load(machine)

    def update(self):
        with open('machine.json', "w") as machine:
            json.dump(self.machine, machine, indent=4)


class System(OpenFile):
    def __init__(self):
        super().__init__()

    def check_stock(self, total_coins, coin):
        if self.machine[coin] >= total_coins:
            self.machine[coin] -= total_coins
            self.update()
            return True
        else:
            return False


    def load_coin(self, coin):
        self.machine[coin] += 100
        self.update()
        print("Machine is full")


    def loading(self):
        x = ""
        y = "🌕"
        while True:
            n = random.randint(1, 3)
            if len(x) <= 20:
                x += y * n
                time.sleep(0.7)
                subprocess.run('clear', shell=True)
                print(x)
            else:
                print('Add coin finish')
                time.sleep(1)
                subprocess.run('clear', shell=True)
                return False

    def effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.019)
        print()

class Screen(System):
    def __init__(self):
        super().__init__()
        # self.machine_list = []
        # self.ask = None

    def coin_(self, bank):
        while True:
            try:
                self.ask = int(input("How many bills do you want to exchange? : "))
            except ValueError:
                # print("Please insert again")
                self.effect("Please insert again")

            else:
                break

        while True:
            # print("Please choose the type of coin")
            self.effect("..." * 10)
            self.effect("Please choose the type of coin")
            self.effect("..." * 10)
            print("1. 5")
            print("2. 10")
            print("3. 𝑬𝑋𝐼𝘛")
            self.effect("___" * 10)
            option = input('Please select your option : ')
            self.effect("___" * 10)
            if option == "1":
                total_coin = (self.ask * bank) // 5
                if self.check_stock(total_coins=total_coin, coin="5"):
                    print("Total of your banknote is: ", self.ask * bank, "baht")
                    print("Total of 5 baht-coin is: ", total_coin, "coins")
                    print('---' * 10)
                    print("Thank you for using our service")
                    print('---' * 10)
                    # break
                    return True
                else:
                    print("Sorry, we don't have enough coins")
                    self.load_coin(coin="5")
                    return self.loading()

            elif option == "2":
                total_coin = (self.ask * bank) // 10
                if self.check_stock(total_coin, "10"):
                    print("Total of your banknote is: ", self.ask * bank, "baht")
                    print("Total of 10 baht-coin is: ", total_coin, "coins")
                    print("Thank you for using our service")
                    return True
                    # break
                else:
                    print("Sorry, we don't have enough coins")
                    self.load_coin(coin="10")
                    return self.loading()

            elif option == "3":
                # break
                return True
            else:
                print("Please insert again")

    # def page1(self):
    #     pass
    #
    # def page2(self):
    #     pass
    #
    # def page3(self):
    #     pass