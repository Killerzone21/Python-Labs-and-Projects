words = ['loop','function','list','variable','string']
def longest(w):
    ind = 0
    long = (len(w[0]))
    for i in range(1,len(w)):
        length =(len(w[i]))
        if long < length:
            long = length
            ind = i
    return w[ind]
def shortest(w):
    short = (len(w[0]))
    ind = 0
    for i in range(1,len(w)):
        length =(len(w[i]))
        if short > length:
            short = length
            ind = i
    return w[ind]
def seven(w):
    ind = []
    for i in range(len(w)):
        length =(len(w[i]))
        if length > 7:
            ind.append(w[i])
    return ind
print(longest(words))
print(shortest(words))
print(seven(words))
