BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
MaleBabys = 0
for line in BabyNames:
    element = line.split(',')
    if element[1] == 'M' and element[2] == '1996':
        MaleBabys = MaleBabys + int(element[4])
print("Number of Male babies born:",MaleBabys)
BabyNames.close()
