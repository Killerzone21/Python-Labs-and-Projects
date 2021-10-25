#**********************  Covert numberdate to letter date.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 12 part 2
#
# Algorithm:
#
#   Assign a counter to exit program
#   Make a new function called Conversion
#       In this function, take the incoming date and split it into a list
#       Assign a new string variable for changing the date
#       Check the first element in the list and assign it the appropriate date
#       If it is 01, add January to the string, if it is 02, add February to the string, etc etc
#       Add the 2nd element in the list the string
#       Finally, add 20 to the string then add the 3rd element to the list.
#   In a loop that continually asks the user for a date:
#       Ask a user for a date and send it to the function
#       Print the converted date and ask if they want to continue
#       If anything but no or n, continue, otherwise, exit the loop by changing the counter to -1
#**********************************************************

counter = 0
   
def Conversion(date):

    WordDate = date.split("/")

    FinalDate = ""

    if WordDate[0] == "01":
        FinalDate = FinalDate + "January"
    elif WordDate[0] == "02":
        FinalDate = FinalDate + "February"
    elif WordDate[0] == "03":
        FinalDate = FinalDate + "March"
    elif WordDate[0] == "04":
        FinalDate = FinalDate + "April"
    elif WordDate[0] == "05":
        FinalDate = FinalDate + "May"
    elif WordDate[0] == "06":
        FinalDate = FinalDate + "June"
    elif WordDate[0] == "07":
        FinalDate = FinalDate + "July"
    elif WordDate[0] == "08":
        FinalDate = FinalDate + "August"
    elif WordDate[0] == "09":
        FinalDate = FinalDate + "September"
    elif WordDate[0] == "10":
        FinalDate = FinalDate + "October"
    elif WordDate[0] == "11":
        FinalDate = FinalDate + "November"
    elif WordDate[0] == "12":
        FinalDate = FinalDate + "December"

    FinalDate = FinalDate + " " + WordDate[1] + ","

    FinalDate = FinalDate + "20" + WordDate[2]

    return FinalDate

while counter != -1:
        date = input("Enter a date in the format xx/xx/xx:")
        print("Here is the Date:", Conversion(date))
        Again = input("Enter another date? Enter 'no' or 'n' to quit:")
        Again.lower()
        if Again == "no" or Again == "n":
            counter = -1
        
5
