#**********************  PasswordInput.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 9
#
# Algorithm:
#   Create a variable to track all cases
#   Create a password length function to test if the password is long enough. Return an error message if not
#   Create an uppercase check function to test if the password contains an uppercase. Return an error message if not
#   Create a lowercase function to test if the password contains a lowercase. Return an error message if not
#   Create an number check function to test if the password contains a number. Return an error message if not
#   Create an password check function to test if the password they typed matches the previous password they wrote. Return an error message if not
#   Print out the requirements for a password which will be accepted.
#   Use the variable created before to test each case. Everytime a case is passed, add one to the counter.
#   Check the counter to see if the password they sent in passed a test. If not, do not do anymore tests. If they did, do the next test case to see if the password will pass it.
#   If they passed the first test, the counter should now be 1 to indicate a passed case. If they pass the 2nd test, the counter should now be 2 and so on.
#   At the end, if they passed all test cases, output a message telling the user their password was accepted!
#**********************************************************
counter = 0

def pswlength(word):
    if len(word) >= 8:
        return True
    else:
        print("Password is not long enough. Password rejected!")

def uppercheck(word):
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i in Uppercase:
            return i in Uppercase
    print("Password is missing an uppercase letter! Password rejected!")

def lowercheck(word):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i in lowercase: 
            return i in lowercase
    print("Password is missing a lowercase letter! Password rejected!")

def numcheck(word):
    numbers = "1234567890"
    for i in word:
        if i in numbers:
            return i in numbers
    print("Password does not contain a number! Password rejected!")

def Pswcheck(First,Second):
    if First == Second:
        return True
    else:
        print("Passwords do not match! Password rejected!")


print("Enter a password following these criteria:")
print("\t \u26AB Must be at least 8 characters long")
print("\t \u26AB Must contain at least one uppercase character")
print("\t \u26AB Must contain at least one lowercase character")
print("\t \u26AB Must contain at least one digit '0' - '9' ")

PasswordOne = input("Please enter a password:")

if pswlength(PasswordOne) == True:
    counter += 1
if counter == 1:
  if uppercheck(PasswordOne) == True:
      counter +=1
if counter == 2:
    if lowercheck(PasswordOne) == True:
        counter += 1
if counter == 3:
    if numcheck(PasswordOne) == True:
        counter += 1
if counter == 4:
    PasswordTwo = input("Please reenter your password:")
    if Pswcheck(PasswordOne,PasswordTwo) == True:
        counter += 1
if counter == 5:
    print("This password is good! Password Accepted!")
    

        
