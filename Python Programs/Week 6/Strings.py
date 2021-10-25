alpha = 'abcdefghijk'[10]
print(alpha)

hello = "hello OUT there"
upHello = hello.upper()
upHello
print(hello.lower())


aStr = "a"
bStr = "b"
newStr = aStr + bStr
print(newStr)

numString = ""
for i in range(1,9):
    numString = numString + str(i)
print(numString)

sz = len(hello)
last = hello[sz-1]

print(last)


def reverseStr(word):
    new = ''
    for i in range(0, len(word)):
        new = new + word[ - (i+1)]
    return new
print(reverseStr("IamTheWalrus"))

prefix = 'JKLMNOPQ'
suffix = 'ack'
for p in prefix:
    if(p == 'O' or p == 'Q'):
        print(p + 'u' + suffix)
    else:
        print(p + suffix)
