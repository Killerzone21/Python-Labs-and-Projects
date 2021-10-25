s1 = "Stop. Who would cross the {0} must answer these questions three".format("Bridge of Death")
print(s1)
s2 = "Ask me the questions, {0}. I am not afraid".format("bridgekeeper")
print(s2)
s3 = "My name is {0}".format("Sir Galahad")
s4 = "My quest is to seek the {0}".format("Holy Grail")
s5 = "My favorite color is {0}".format("blue")
print(s3, s4, s5)


s1 = "{0} #{1} has now tromped on {2}".format("Godzilla", 5,  "Mothra")
print(s1)

name = "Alice"
age = 10
s2 = "I am {1} and I am {0} years old.".format(age,name)
print(s2)


pi = 3.1415926
s1 = "The value of pi to four decimal places is {0:.4f}".format(pi)
print(s1)

letter = """
Dear {0} {1},
    {0}, I watched you in {2} and I’m a big fan!
Sincerely Yours
    """
print(letter.format("Gal", "Gadot", "Wonder Woman"))
print(letter.format("Chadwick", "Boseman", "Black Panther"))

layout = "{0:>4} {1:>6} {2:>6} {3:>6} {4:>12} {5:>21}"
print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20") )
for i in range(1,11):
         print(layout.format(i,  i**2, i**3, i**5,  i**10,  i**20) )

print()

n1 = 1024
print("The decimal value of n1 is {0} and hex value is {0:x}".format(n1))

print()

layout = "{0:>2} {1:>2} {2:>2} {3:>2} {4:>2} {5:>2} {6:>2} {7:>2} {8:>3} {9:>3} {10:>3} {11:>3}"
print(layout.format("\t  1", "2", "3", "4", "5","6","7","8","9","10","11","12") )
print("  :-----------------------------------------------")
for i in range(1,13):
    print(i, ":\t", layout.format(i*1, i*2, i*3, i*4,  i*5,  i*6, i*7, i*8, i*9, i*10, i*11, i*12) )

print()

for i in range(0,49):
    print("The decimal value of n1 is {0} and hex value is {0:x}".format(i))
