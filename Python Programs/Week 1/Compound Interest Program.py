#**********************  CompoundInterestProgram.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: In-class Assignment 1
#
# Algorithm:
#   Prompt user for years the money will be compounded
#   Assign variables from equation to individual numbers
#   Apply order of operations
#   Display the final amount rounded to two decimal places
#**********************************************************

t = int(input("Enter the number of years the money will be compounded for: "))
P = 10000                                               #Assign your variables
n = 12
r = .08

FinalNumber = P * ( 1 + r/n)**(n*t)                     #Find the final number
FinalNumber = str(round(FinalNumber, 2))

print("Your compounded Interest is:", FinalNumber)

