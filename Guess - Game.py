# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:58:14 2022

The number Guessing Game between 1 and 10

@author: Ellie Nia
"""
from random import randint
TotalPoint = 0


def GenerateGuess():           #A function that generate a random guess
    return(randint(1,10))


def CheckGuess(user,computer):          #A function that takes a userguess and secret computer guess
    global TotalPoint                   #Use global keyword to use the totalpoint variable
    
    if  user == computer:               #Check if user guess and computer guess is same or not
        TotalPoint = TotalPoint + 5
        return True
    else:
        return False
    
    
def main():
    print("Lets play the number Guessing Game")
    userguess = 0
    computerguess = 0
    
    userguess = int(input("Make a guess: "))
    computerguess = GenerateGuess()             #Call the generateguess function to return a value in the variable
    result = CheckGuess(userguess,computerguess)    #Call the checkguess function to return a boolian value in the variable
    
    if result == True:                              #Check if checkguess funtion returns True, display congrats and show the total point
        print("Congrats, you have",TotalPoint,"point")
    else:
        print("you lost")                       #Check if checkguss returns False, display you lost
        playagain = input("If you want to play again type yes otherwise type No: ")        #Ask if user wants to play again, type yes and call the main
        if playagain == "yes":
            main()
        else:
             print("Good Bye, your total point is: ", TotalPoint)           #if user doesn't want to play, display goodbye and show the total point
        
main()
        