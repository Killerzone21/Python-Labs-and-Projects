#import random

#answer = input("Do you want to roll dice?")
#while answer == 'yes' or answer =='y':
#    randomNum = random.randint(1,6)
#    print("The number you rolled is:", randomNum)
#    answer = input("Do you want to roll dice?")

#year = int(input("To find an age enter a year, or type 0 to stop"))
#while year != 0:
#    print("A person born in", year, "is approximately", 2019 - year, "years old")
#    year = int(input("To find an age enter a year, or type 0 to stop"))
#print("Goodbye")

#n = int(input("To find the sum of the first n integers, enter a value of n:"))
#total = 0
#for i in range(n + 1):
#    total = total + i
#print("The sum of the first",n,"integers is: ", total)

n = int(input("To find the sum of the first n integers, enter a value of n, Enter a negative number to exit:"))
total = 0

while n > -1:
    total = total + n
    n = n -1
    if(n == 0):
        print("The sum of the first",n,"integers is: ", total)
        total = 0
        n = int(input("To find the sum of the first n integers, enter a value of n, Enter a negative number to exit:"))
print("Goodbye")
