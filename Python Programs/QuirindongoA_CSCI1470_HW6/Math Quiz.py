#**********************  MathQuiz.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 6
#
# Algorithm:
#   Import random and define varibles for User score, what problem they are on and how many problems they have gone through
#   While the user is still taking the test, assign them the appropriate problems:
#       Starting with addition, randomize 2 numbers and task the user to solve it. Have the computer solve it itself and compare answers. Remember to only compare one problem at a time.
#       Print the problem before the user and if they guess correctly, notify them and add a point to their score. Do the opposite if incorrect.
#       Add to the number of problems they have done and what problem they are on. If they have gone through 2 problems of a single math equation, assign them a new problem with a different operator.
#       Otherwise, keep asking the user a problem with the current operator
#       Do the same for Subtraction, Multiplication, Division and Modulus
#       Let the user know that division is floor division or only the integar value is being asked for. Make sure they fully understand the problem being asked and what answer is being expected.
#       Let the user know how the Modulus problem is being asked and provide an example. Do not tell them in computer terms because they may not know.
#       While still in the loop before it ends, provide the user his final score and ask if they want to retake the quiz. Exit the loop if their answer is not "Yes" or "Y"
#   Thank them for taking the quiz!
#**********************************************************
import random

score = 0
count = 0
problem = 1

while count != 10:                              #If Count is less than 10, User is still taking quiz
    while problem < 3:                          #First 2 problems are addition
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("What is",num1,"+",num2,"?")
        Userguess = int(input("Your answer:"))
        answer = num1 + num2
        if Userguess == answer:
            print("Correct!")
            score = score + 1
        if Userguess != answer:
            print("Incorrect!")
        problem = problem + 1
        count= count + 1
    while problem < 5:                          #Next 2 problems are subtraction
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("What is",num1,"-",num2,"?")
        Userguess = int(input("Your answer:"))
        answer = num1 - num2
        if Userguess == answer:
            print("Correct!")
            score = score + 1
        if Userguess != answer:
            print("Incorrect!")
        problem = problem + 1
        count= count + 1
    while problem < 7:                          #Next 2 problems are Multiplication
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("What is",num1,"*",num2,"?")
        Userguess = int(input("Your answer:"))
        answer = num1 * num2
        if Userguess == answer:
            print("Correct!")
            score = score + 1
        if Userguess != answer:
            print("Incorrect!")
        problem = problem + 1
        count= count + 1
    while problem < 9:                          #Next 2 problems are division
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("What is",num1,"/",num2,"?: Do only floor division or whole values. No decimals")
        Userguess = int(input("Your answer:"))
        answer = num1 // num2
        if Userguess == answer:
            print("Correct!")
            score = score + 1
        if Userguess != answer:
            print("Incorrect!")
        problem = problem + 1
        count= count + 1
    while problem < 11:                          #Next 2 problems are modulus
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        print("What is the remainder when",num1,"is divided into",num2,"one time? Ex: 3 % 2 is 1 because 3 - 2 leaves 1 left over. 4 % 19 would be 4 because 4 - 0 leaves 4 left over.")
        Userguess = int(input("Your answer:"))
        answer = num1 % num2
        if Userguess == answer:
            print("Correct!")
            score = score + 1
        if Userguess != answer:
            print("Incorrect!")
        problem = problem + 1
        count= count + 1
    print("Your final score is:",score)
    Retake = input("Do you want to take the quiz again? Enter yes or y to retake it:")
    if(Retake.lower() == 'yes' or Retake.lower() == 'y'):
        problem = 1
        count = 0
        score = 0
print("Thanks for taking the test!")


