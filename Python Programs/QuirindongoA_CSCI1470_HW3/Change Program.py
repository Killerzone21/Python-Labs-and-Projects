#**********************  ChangeProgram.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 3
#
# Algorithm:
#   Ask User for cost of item and how much they are paying for it. Error check if they enter an invalid number or payment is not enough
#   Calculate the change and round it to appropriate money value (2 decimal places)
#   Assign neccessary variables (Dollars, Dimes, Nickles) and adjust change into the pennies value of owned amount (i.e. 1.98 = 198 pennies)
#   Check if they are paying enough for the item, else notify the user the amount paid is not enough and output error message. Do nothing else
#   In a while loop, check to see if they don't need change first, else caculate the final change.
#   Assign Dollars to the integar value of change divided by 100 (100 pennies in a dollar) then multiply that integar by 100 and subtract it from change
#   Assign Dimes to the integar value of change divided by 10 (10 pennies in a dime) then multiply that integar by 10 and subtract it from change
#   Assign Nickles to the integar value of change divided by 5 (5 pennies in a nickle) then multiply that integar by 5 and subtract it from change
#   Leftover Change is pennies.
#   Print out the amount of Change in Dollars, Dimes, Nickles and Pennies Value
#   Assign Change to -1 after so that you can exit the loop if user does not wish to continue
#   Ask User for the cost of new item
#   Check to see if User entered an appropriate number, else do nothing more and print out final message
#   If User entered appropriate amount (Greater than 0), ask for new payment value to cover cost. Redo all the caculations again and assign the new change value to restart loop. Reassign all variables back to 0
#   Continue this until User enters a negative number or 0
#**********************************************************

Cost = float(input("How much does the item cost?"))
while(Cost < 1):
    print("Please enter an approriate value for the cost of item:")
    Cost = float(input("How much does the item cost?"))

Payment = float(input("How much are you paying for the item?"))

Change = Payment - Cost

while(Change < 0):
    print("Your payment does not cover the cost of the item.")
    Payment = float(input("Please enter an appropriate value to cover the cost of item:"))
    Change = Payment - Cost

Change = round(Change,2)

Nickles = 0
Dimes = 0
Dollars = 0
Change = Change * 100                  #Convert change into total pennies
while(Change >= 0):
    if(Change == 0):                    #Check if they need change first
        print("No change!")
    else:
        Dollars = Change//100              #Calculate the amount of dollars first
        Change = Change - (Dollars * 100)
        Dimes = Change//10
        Change = Change - (Dimes * 10)
        Nickles = Change//5
        Change = Change - (Nickles * 5)
        print("Thank you for your purchase! Your change is:", int(Dollars),
              "dollar bills,", int(Dimes), "dimes,", int(Nickles),"nickles,",
               int(Change), "pennies.")
    Change = -1
    Cost = float(input("Enter the cost of another item. Enter a negative number or zero if you wish to stop:"))
    if(Cost > 0):                        #Check if they wish to stop
        Payment = float(input("How much are you paying for the item?"))
        if(Payment >= Cost):
            Change = Payment - Cost
            Nickles = 0
            Dimes = 0
            Dollars = 0
            Change = Change * 100
        else:
            print("Your payment does not cover the cost of the item.")
            Change = -1
            print("")
    print("Thank you for your business")    
          
    
