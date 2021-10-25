#**********************  AlphabeticTelephoneTranslator.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 7
#
# Algorithm:
#   Define a Convert Function to handle Coverting Alpha Chars to Numbers
#   In the function, convert the incoming string to uppercases and create a new string for the converted numbers.
#   For each character in the original string(the one sent in), do the following:
#       First, Check the char for a letter. If the letter is A, B or C, add the number 2 to the string.
#       For D, E and F characters, add the number 3 to the string.
#       For G, H and I characters, add the number 4 to the string.
#       For J, K and L characters, add the number 5 to the string.
#       For M, N and O characters, add the number 6 to the string.
#       For P, Q, R and S characters, add the number 7 to the string.
#       For T, U, and V characters, add the number 8 to the string.
#       For W, X, Y and Z characters, add the number 9 to the string.
#       If the incoming character is not a letter, then we assume it is a number or a hyphen. Add it to the string.
#   You can now ask the user for a number. It should convert any telephone number with alpha characters to numbers. Make sure to convert the number they input to a string.
#   Keep asking the user until they decide to quit.
#**********************************************************

def Convert(phoneNum):
    phoneNum = phoneNum.upper()
    FinalNum = ""

    for i in range(len(phoneNum)):
        if phoneNum[i] == 'A' or phoneNum[i] == 'B' or phoneNum[i] == 'C':
            FinalNum = FinalNum + '2'
        elif phoneNum[i] == 'D' or phoneNum[i] == 'E' or phoneNum[i] == 'F':
            FinalNum = FinalNum + '3'
        elif phoneNum[i] == 'G' or phoneNum[i] == 'H' or phoneNum[i] == 'I':
            FinalNum = FinalNum + '4'
        elif phoneNum[i] == 'J' or phoneNum[i] == 'K' or phoneNum[i] == 'L':
            FinalNum = FinalNum + '5'
        elif phoneNum[i] == 'M' or phoneNum[i] == 'N' or phoneNum[i] == 'O':
            FinalNum = FinalNum + '6'
        elif phoneNum[i] == 'P' or phoneNum[i] == 'Q' or phoneNum[i] == 'R' or phoneNum[i] == 'S':
            FinalNum = FinalNum + '7'
        elif phoneNum[i] == 'T' or phoneNum[i] == 'U' or phoneNum[i] == 'V':
            FinalNum = FinalNum + '8'
        elif phoneNum[i] == 'W' or phoneNum[i] == 'X' or phoneNum[i] == 'Y' or phoneNum[i] == 'Z':
            FinalNum = FinalNum + '9'
        else:
            FinalNum = FinalNum + phoneNum[i]
    return FinalNum

counter = 0

while counter != -1:
    TeleNum = str(input("Enter a phone Number you wish to convert to numeric:"))
    print(Convert(TeleNum))
    Again = str(input("Wish to go again? Enter y or yes to continue"))
    if(Again.lower() != 'y' and Again.lower() != 'yes'):
       counter = -1

print("Goodbye!")
