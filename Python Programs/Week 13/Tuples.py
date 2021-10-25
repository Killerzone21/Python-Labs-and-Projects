SomeList = ("Julia", "Roberts", 1967, "Atlanta, Georgia","Actress")

for index in range(len(SomeList)):
    print(SomeList[index])

count = 0

babyFile = open("TXBabyNames.txt")
for line in babyFile:
    elements = line.split(",")
    (state,gender,year,firstName,freq) = elements
    if int(year) >= 1996 and int(year) <= (1996 + 10):
        if firstName == "Alexander":
            count = count + 1
print("The total number of babies named Alexander is " + str(count))
