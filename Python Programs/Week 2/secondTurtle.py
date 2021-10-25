import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Bepo!")

bepo = turtle.Turtle()

bepo.color("purple")
bepo.pensize(3)

bepo.forward(50)
bepo.left(120)

bepo.penup()
bepo.forward(50)
bepo.pendown()
bepo.backward(200)


wn.mainloop()
