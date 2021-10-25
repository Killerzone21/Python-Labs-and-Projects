#**********************  SecretMessage.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 12
#
# Algorithm:
#
#   Assign a counter to exit program
#   Make a new function called decode Message
#       In this function, take the incoming message and split it into a list
#       Assign a new string variable for decoding the message
#       In a for loop:
#           Add the first letter from each word in the list to the string variable
#       Return the decoded message
#   In a loop that continually asks the user for a message:
#       Ask a user for a message and send it to the function
#       Print the decoded message and ask if they want to continue
#       If anything but no or n, continue, otherwise, exit the loop by changing the counter to -1
#**********************************************************

counter = 0
   
def decodeMessage(Message):

    ListofWords = Message.split()

    decode = ""

    for x in ListofWords:
        decode = decode + x[0]

    return decode

while counter != -1:
        Message = input("Enter a message:")
        print("Here is the decoded message:", decodeMessage(Message))
        Again = input("Enter another message? Enter 'no' or 'n' to quit:")
        Again.lower()
        if Again == "no" or Again == "n":
            counter = -1
        
5
