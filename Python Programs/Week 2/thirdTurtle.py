import turtle
scrn1 = turtle.Screen()
scrn1.bgcolor("lightgreen")
scrn1.title("Hello, yourName!")
bepo = turtle.Turtle()
bepo.shape("turtle")
bepo.color("red")
bepo.stamp()
bepo.color("white")
bepo.penup()
bepo.forward(20)
size = 20
for i in range(30):
    bepo.stamp()
    size = size + 3
    bepo.forward(size)
    bepo.right(24)
bepo.color("blue")

bepo1 = turtle.Turtle()
bepo2 = turtle.Turtle()

bepo1.pensize(2)
bepo2.pensize(2)
    
for i in range(3):
    bepo1.forward(40)
    bepo1.left(120)

for i in range(4):
    bepo2.forward(-50)
    bepo2.left(-90)

scrn1.mainloop()
