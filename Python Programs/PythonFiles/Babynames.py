BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
FemaleCounter = 0
for line in BabyNames:
    element = line.split(',')
    if element[1] == 'F':
        FemaleCounter += 1
print("The number of female baby names is:",FemaleCounter)
BabyNames.close()
