#**********************  BoxingCompetition.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 4
#
# Algorithm:
#   Define all necessary variables beforehand
#   Ask User for the weight of his first competitor
#   Assign the competitor to an appropriate category and add his weight to your average variable
#   Repeat the process for all competitors the user adds until he enters a 0 or negative number
#   Assign a new variable and caculate the total number of competitors you have from the appropriate categories
#   Calulate the average weight of all competitors. Error check if there is no competitors to prevent dividing by zero
#   Check if there is only 1 competitor in a specific category. If so, move them up to the next category. Do not do this for the highest possible Category (Can't go any further)
#   Print the average weight of all competitors
#   Print out the different categories and how many competitors are in each category
#**********************************************************

Welterweight = 0
Lightweight = 0
Featherweight = 0
Bantamweight = 0
TooLow = 0
TooHigh = 0
AverageofWeight = 0

Compweight = int(input("Enter the weight of the competitor: "))

while Compweight > 1:
    if Compweight > 60 and Compweight < 65:
        Welterweight = Welterweight + 1
        AverageofWeight = AverageofWeight + Compweight
    elif Compweight > 57 and Compweight < 61:
        Lightweight = Lightweight + 1
        AverageofWeight = AverageofWeight + Compweight
    elif Compweight > 54 and Compweight < 58:
        Featherweight = Featherweight + 1
        AverageofWeight = AverageofWeight + Compweight
    elif Compweight > 50 and Compweight < 55:
        Bantamweight = Bantamweight + 1
        AverageofWeight = AverageofWeight + Compweight
    else:
        if Compweight < 51:
            TooLow = TooLow + 1
        else:
            TooHigh = TooHigh + 1
    Compweight = int(input("Enter the weight of the competitor, Enter a Zero or Negative number to end: "))

TotalComps = Welterweight + Lightweight + Featherweight + Bantamweight
if(TotalComps > 0):
    AverageofWeight = AverageofWeight//TotalComps

if Bantamweight == 1:
    Bantamweight = 0
    Featherweight = Featherweight + 1
if Featherweight == 1:
    Featherweight = 0
    Lightweight = Lightweight + 1
if Lightweight == 1:
    Lightweight = 0
    Welterweight = Welterweight + 1

print("")
print("The Average weight of all competitors in this competition is:", AverageofWeight)
print("")
print("The number of competitors we have in each category is:")
print("")
if Welterweight > 0:
    print("Welterweight ", Welterweight)
if Lightweight > 0:
    print("Lightweight ", Lightweight)
if Featherweight > 0:
    print("Featherweight ", Featherweight)
if Bantamweight > 0:
    print("Bantamweight ", Bantamweight)
if(Welterweight == 0 and Lightweight == 0 and Featherweight == 0 and Bantamweight == 0):
    print("No competitors")
