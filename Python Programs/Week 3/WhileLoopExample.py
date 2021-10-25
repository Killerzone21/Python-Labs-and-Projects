index = 0
print("While Loop")
while index <= 5:
    print(index)
    index = index + 1

print("For Loop")    
for index in range(6):
    print(index)

print("Another while loop")
count = 1
while count <= 5:
    print(count)
    count = count + 2

print("Another For Loop")
count = 1
for count in range (1,6,2):
    print(count)

    

print("Another while loop")
number = int(input("What number do you want to print? Enter 0 to stop "))
count = 0
while number >= 1:
    print(number)
    count = count + 1
    number = int(input("What number do you want to print? Enter 0 to stop "))
print("You print", count, "numbers")    




