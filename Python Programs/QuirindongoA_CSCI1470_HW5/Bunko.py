#**********************  Bunko.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 5
#
# Algorithm:
#   Import random and define varibles for 3 dice, 2 player scores, which turn it is and whether you are repeating a turn
#   Define your take_turn function importing the current players score using the following rules:
#       Roll 3 dice and compare them to each other. Print their individual values.
#       If all 3 dice equal 6, return a score 21 and give bunko to the current player.
#       Else if 2 of the dice equal 6, return a score of 5 and allow the player to keep rolling
#       Else if 1 of the dice equal 6, return a score of 1 and allow the player to keep rolling
#       Else if all 3 dice equal the same value but the value is not 6, do not give the player any points but allow them to roll again
#       Else return a score of 0 and switch turns
#   After the player takes their turn, add the amount of points they earn to their current score, and keep track of it
#   Continue playing until one of the players gets a score of 21 or higher, then declare the player who got 21 or higher the winner
#**********************************************************
import random

Die1 = 0
Die2 = 0
Die3 = 0

Player1Score = 0
Player2Score = 0

CurrentTurn = 1

RepeatTurn = 0

def take_turn(score):
    Die1 = random.randint(1,6)
    Die2 = random.randint(1,6)
    Die3 = random.randint(1,6)
    print(Die1,Die2,Die3)
    if Die1 == 6 and Die2 == 6 and Die3 == 6:
        return 21
    elif Die1 == 6 and (Die1 == Die3 or Die1 == Die2):      #If die 1 is 6 and either Die 2 or Die 3 are 6
        return 5
    elif Die2 == 6 and Die3 == 6:                        #If Die 2 and Die 3 are 6
        return 5
    elif Die1 == 6 or Die2 == 6 or Die3 == 6:
        return 1
    elif Die1 == Die2 and Die2 == Die3:                 #Gets to repeat turn if all dice are same
        return -1
    else:
        return 0

while Player1Score < 21 and Player2Score < 21:
    if CurrentTurn == 1:
        answer = input("You ready to take your turn player 1?")
        Score = take_turn(Player1Score)
        if Score == -1:
            RepeatTurn = Score
            Score = 0
        Player1Score = Player1Score + Score
        print("You now have:", Player1Score)
        if Score == 1 or Score == 5 or RepeatTurn == -1:
            CurrentTurn = 1
            RepeatTurn = 0
        else:
            CurrentTurn = 2
    else:
        answer = input("You ready to take your turn player 2?")
        Score = take_turn(Player2Score)
        if Score == -1:
            RepeatTurn = Score
            Score = 0
        Player2Score = Player2Score + Score
        print("You now have:", Player2Score)
        if Score == 1 or Score == 5 or RepeatTurn == -1:
            CurrentTurn = 2
            RepeatTurn = 0
        else:
            CurrentTurn = 1

if Player1Score >= 21:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
