ReadFile = open("TaxManMax.txt","r")
NewFile = open("RhymeswithMax.txt", "w")

for line in ReadFile:
    element = line.split(' ')
    for word in element:
        if "ax" in word or "acks" in word:
            print(word)
            NewFile.write(word)
            NewFile.write("\n")

NewFile.close()    
ReadFile.close()
    
