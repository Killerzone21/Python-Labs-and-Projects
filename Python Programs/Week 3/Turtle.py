import turtle
window = turtle.Screen()
turtle.setup(300,300)
window.bgcolor("green")

squirtle = turtle.Turtle()
squirtle.shape("arrow")
squirtle.color("purple")
squirtle.pensize(4)
squirtle.penup()
squirtle.setpos(-100,50)
squirtle.pendown()

for i in range(4):
    squirtle.forward(50)
    squirtle.left(90)

squirtle.penup()
squirtle.forward(100)
squirtle.pendown()

for i in range(8):
    squirtle.forward(100)
    squirtle.left(225)
    
squirtle.penup()
squirtle.setpos(-100,-75)
squirtle.pendown()

for i in range(1,38):
    squirtle.forward(100)
    squirtle.left(175)

squirtle.reset()
for i in range(1,20):
    squirtle.forward(100)
    squirtle.left(95)

    
