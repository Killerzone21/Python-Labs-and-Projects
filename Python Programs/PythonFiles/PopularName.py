BabyNames = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\TXBabyNames.txt')
ValMax = 0
counter = 0
for line in BabyNames:
    element = line.split(',')
    if element[1] == 'F' and element[2] == '1925':
        if int(element[4]) > ValMax:
            PopName = element[3]
            ValMax = int(element[4])
    if element[1] == 'M' and element[2] == '1925' and element[3] == PopName:
            counter = element[4]

print("Number of Male",PopName,"is:",counter,"in the year 1925")
BabyNames.close()
