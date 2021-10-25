BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
counter = 0
for line in BabyNames:
    element = line.split(',')
    if element[1] == 'M' and element[2] == '1996' and element[3] == 'Alexander':
        counter = element[4]

print("Number of Alexander's born in 1996 is:",counter)
BabyNames.close()
