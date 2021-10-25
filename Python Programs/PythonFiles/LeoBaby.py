BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
Leonumber = 0
years = []
for line in BabyNames:
    element = line.split(',')
    if element[3] == 'Leo' and element[1] == 'M':
        Leonumber += 1
        if element[2] not in years:
            years.append(element[2])

print("Number of Leos:", Leonumber)
print("Years Leo was born:", years)
BabyNames.close()
