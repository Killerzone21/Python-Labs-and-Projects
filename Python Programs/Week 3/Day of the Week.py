Day = int(input("Enter a number between 0 and 6, enter a number less than 0 or greater than 6 to end it:"))

while Day > -1 and Day < 7:
    if Day == 0:
        print("Sunday")
    elif Day == 1:
        print("Monday")
    elif Day == 2:
        print("Tuesday")
    elif Day == 3:
        print("Wednesday")
    elif Day == 4:
        print("Thursday")
    elif Day == 5:
        print("Friday")
    elif Day == 6:
        print("Saturday")
    Day = int(input("Enter a number between 0 and 6, enter a number less than 0 or greater than 6 to end it:"))

print("The end")
    
