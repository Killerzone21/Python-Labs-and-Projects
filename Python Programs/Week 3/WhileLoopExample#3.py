number = int(input("Enter the grades you want to average: Enter any negative number to stop "))
count = 0
Grades = 0
while number >= 0:
    Grades = number + Grades
    count = count + 1
    number = int(input("Enter another grade: Enter any negative number to stop "))
if(count == 0):
    print("You did not enter any grades to be averaged!")
else:
    Average = Grades / count
    print("Your average is:", Average)
