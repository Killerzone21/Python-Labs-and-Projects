#**********************  WeeklyPay.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 1
#
# Algorithm:
#   Prompt user for their name, hourly wage, total regular hours, total overtime hours
#   Multiply Hourly wage by regular hours
#   Multiply Hourly wage by 1.5 then multiply that by overtime hours
#   Add regular hour wage to overtime hour wage then round to 2 decimal places (cents)
#   Display Employee's name alongside their weekly payp
#**********************************************************
NameOfEmployee = input("Enter your name:")
HourlyWage = float(input("Enter the hourly wage:"))
TotalRegHour = float(input("Enter the total amount of hours:"))
TotalOverHour = float(input("Enter any overtime hours:"))

WeeklyPay = (HourlyWage * TotalRegHour) + ((HourlyWage * 1.5) * TotalOverHour)
WeeklyPay = round(WeeklyPay, 2)

print(NameOfEmployee, ", your pay for this week is", WeeklyPay)
