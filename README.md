The project name "The Automatic coin exchange machine"

The Automatic coin exchange machine is a machine that can exchange bills into coins which are the only 20, 50, 100 baht bills that can be exchanged to 5 or 10 baht coins.

Having the six files to run the program which is two files about writing the code and four files for the information.

Coding file are automaticmachine.py and welcome_page.py

The automaticmachine.py file have “three” classes
    1. Open File class that uses the attribute to read the file and use the method  to write(update) file.
    2. System class is about the writing of input which have check_stock that is the method of checking the coins in the machine, load_coin to add the coin if the coins in the machine are depleted, loading is showing output while the machine add the coins in the stock and effect to showing the effect of printing the word
    3. Screen class is about showing output of a program on the screen which has one method; coin.

The welcome_page.py file is using the Screen class and writing some output and using this file to run the program or run in terminal.

Information file are bills.txt, coins.txt, machine.json and README

bills.txt file is the information of bills that can be used in the machine.
coins.txt is the information of coins that can be used in the machine.
machine.json is the stock of coins that the method ‘load_coin’ will add the coins into this file.
README is explaining the project.