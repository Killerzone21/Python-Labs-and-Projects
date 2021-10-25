def avg(x,y,z):
    print((x+y+z)/3)

avg(1,2,3)
avg(5,7,4)

def has_no_e(x):
    for i in x:
        return "e" not in x

print(has_no_e("Apple"))
print(has_no_e("Cowboy"))
print(has_no_e("Star Trek"))

def count_e(sentence):
    count = 0
    for x in sentence:
        if x == "e":
            count = count + 1
    print(count)

count_e("Please help me im falling in love")
count_e("lalala, I am singing everyone's favorite lyrics")


def no_blanks(x):
    newword = ""
    space = " "
    for i in x:
        if i not in space:
            newword += i
    print(newword)

no_blanks("help me")
no_blanks("help    me I am    falling")

def index_letter(x,y):
    letter = y
    p = 0
    for i in x:
        if i == letter:
            return p
        p += 1

print(index_letter("Brown is a color", "z"))
print(index_letter("the quick brown fox", "q"))

def no_punctuations(x):
    newword = ""
    punc = ",.;:?"
    for i in x:
        if i not in punc:
            newword += i
    print(newword)

no_punctuations("I am helpless? Can you, help me:!")
no_punctuations("I live in this world,: They have no hold over me!?")

def isMultiple(x,y):
    return y % x == 0

print(isMultiple(2,4))
print(isMultiple(8,80))
print(isMultiple(12,144))

def factorial(x):
    answer = 1
    while x > 0:
            answer = x * answer
            x = x - 1
    print(answer)

factorial(5)

def floyd(x):
    number = 1
    for i in range(1,x):
        for j in range(1, i + 1):
           print(number, end=' ')
           number = number + 1
        print()
        
floyd(5)











