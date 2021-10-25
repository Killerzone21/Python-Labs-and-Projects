colors = ['red','blue','green','yellow','purple']
def end(c):
    first = c[0]
    last = c[len(c)-1]
    return (first,last)
print(end(colors))
def middle(c): 
    c.remove(c[0])
    c.remove(c[len(c)-1])
    return c
print(middle(colors))
