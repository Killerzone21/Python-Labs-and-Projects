myFile = open("haiku.txt", "w")
myFile.write("I have a sweet dog \n")
myFile.write("Who loves to lay in the sun \n")
myFile.write("I’m so glad he’s mine \n")
myFile.close() 


print("This is a backslash \ ")
print("This is a backslash \\")
print("This is a new line \n")
print("This is a horizontal tab \t see?")


myFile = open("haiku.txt", "r")
words = myFile.read()
print(words)

myFile = open("haiku.txt","a")
myFile.write("..No longer haiku! \n")
myFile.close()


f = open("sep.txt", "r")
words = f.read().split()
counter = 0
for w in words:
    print(w)
    counter = counter + 1

print("Number of words:",counter)
f.close()
