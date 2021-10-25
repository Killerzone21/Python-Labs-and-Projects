def reverseStr(word):
    new = ''
    for i in range(0, len(word)):
        new = new + word[ - (i+1)]
    return new

def palindrome(word):
    if word.lower() == reverseStr(word.lower()):
        print("Is a Palindrome")
    else:
        print("Is not a Palindrome")

palindrome("tacocat")
