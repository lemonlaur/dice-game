# Lauren Cook
# feb 14 2022
# dice game

from random import randint
from time import sleep

money = 100
while money > 0 or choice == "q" :
    def user_guess():
        user_num = int(input("Guess a number between 2 - 12:"))
        return(user_num)
    
    def wager_bet():
        wager_num = int(input("How much would you like to wager?"))
        return(wager_num)

    def roll_dice():
        first_roll = randint(1,6)
        second_roll = randint(1,6)
        total = first_roll + second_roll
        sleep (1)
        wager = wager_bet()
            if wager > money and wager < 0:
            print("You cannot wager that.")
        guess = user_guess()
            if guess >= 12 and guess < 2:
            print("Choose a correct number :")
    
        if guess == total:
            money + wager
            print("User wins")
        else:
            money - wager
            print("User lost")
