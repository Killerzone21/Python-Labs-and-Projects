BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
BabyName = str(input("What baby name do you want?:"))
years = int(input("What years are you looking for:"))
BabyName[0].upper()
counter = 0

for line in BabyNames:
    element = line.split(',')
    for i in range(0,10):
        if element[3] == BabyName and element[2] == str(years + i) and element[1] == 'F':
            counter = counter + int(element[4])     

print("Number of ",BabyName," in the span of years:",years,"-",years+9,"is:",counter)
BabyNames.close()
