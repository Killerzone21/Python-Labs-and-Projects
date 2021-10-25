stuff = ['a','c','b','d','b']
def has_duplicates(s):
    for i in range(len(s)):
        for j in range (i+1,len(s)):
            if s[i] == s[j]:
                return s[i]
    return "none"
def remove_duplicates(s):
    newL = []
    for i in range(len(s)):
        newL.append(s[i])
        for j in range (i+1,len(s)):
            if s[i] == s[j]:
                newL.remove(s[j])
    return newL
print(has_duplicates(stuff))
print(remove_duplicates(stuff))
