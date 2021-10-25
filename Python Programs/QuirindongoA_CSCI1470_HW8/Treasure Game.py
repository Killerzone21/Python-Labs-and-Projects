
#**********************  TreasureGame.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Homework Assignment # 8
#
# Algorithm:
#   Import random and turtle for drawing graphics and determining the treasure's location randomly.
#   Create a turtle screen, your 2 turtles and create the game border for the player to play in using one of the turtles. Hide that turtle afterwards to remove clutter.
#   Randomly assign the player's starting turtle location and the treasure's starting location. Make sure to assign an appropriate size to the box. Also, make sure the player's turtle does not draw lines on the screen 
#   Create varibles for checking player's position within th game border and whether they found the treasure or not. Then while in the loop:
#       Check to see if the player made a bad move or not. Notify the player and ask them for a new movement type (forward or turning).
#       If the player made a legal move, continue to ask them what kind of move they want. Make sure to specify specific numerals for what kind of move they want. 0 = forward, 1 is left turn and 2 is right turn.
#       Since turning will not make the player move out of bounds, no error checking is necessary. Just turn the player the direction they asked for and notify them if there is a max value.
#       If the player is moving forward, ask how far they want and check their new position. If it is out of bounds, move them back and notify them.
#       After the player has made a move, check to see if their new position is within the treasure box's boundaries.
#       If the player is within the boundaries, end the loop.
#       Otherwise, play continues until the player moves within the box's boundaries.
#   If the player found the boundaries, clear the screen, and display an image telling them they won!
#**********************************************************
import random
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

bepo = turtle.Turtle()
player = turtle.Turtle()

player.color("Blue")

bepo.shape("turtle")
bepo.color("red")

bepo.penup()

bepo.setpos(-350,300)                               #Set the playing field for player
bepo.pendown()
bepo.setpos(350,300)
bepo.setpos(350,-275)
bepo.setpos(-350,-275)
bepo.setpos(-350,300)

bepo.ht()

playerX = random.randint(-325,325)                  #Set the player's starting position
playerY = random.randint(-250,275)

player.penup()
player.setpos(playerX,playerY)

x1 = random.randint(-275,275)                       #Initial starting position for treasure's x
y1 = random.randint(-200,225)                       #Initial starting position for treasure's y

x2 = x1 + 50                                        #Set the opposite corner of the square       
y2 = y1 - 50

encounter = -1
BadMovement = 0

while encounter == -1:
    if BadMovement == -1:        
        BadMovement = 0  
        MoveType = int(turtle.numinput("Player Movement", "Invalid move, going off the playing field. Try again: 0 = forward, 1 = turn left, 2 = turn right", default=None, minval = 0, maxval = 2))
    else:
        MoveType = int(turtle.numinput("Player Movement", "Do you want to move forward or turn? 0 = forward, 1 = turn left, 2 = turn right", default = None, minval = 0, maxval = 2))
    if MoveType == 0:
        movement = int(turtle.numinput("Player Movement", "How far do you want to go: 200 is max distance", default=None, minval = 0, maxval = 200))
        player.forward(movement)
        playerposX = player.xcor()                          #New variable to determine player's position
        playerposY = player.ycor()
  
        if playerposX > 350 or playerposY > 300 or playerposX < -350 or playerposY < -275:                 #Is the player going off screen?
            BadMovement = -1
            player.forward(movement*-1)
            
    if MoveType == 1:
            movement = int(turtle.numinput("Player Movement", "How far do you want to turn? 90 is a full left turn, 180 turns you around.", default=None, minval = 0, maxval = 180))
            player.left(movement)
    if MoveType == 2:
            movement = int(turtle.numinput("Player Movement", "How far do you want to turn? 90 is a full right turn, 180 turns you around.", default=None, minval = 0, maxval = 180))
            player.right(movement)
            
    playerposX = player.xcor()
    playerposY = player.ycor()
    
    if playerposX > x1 and playerposX < x2 and playerposY > y2 and playerposY < y1:  #Is the player within the boundaries of the treasure?
        encounter = 0

wn.clear()
wn.bgpic("index.png")                               #You win!
wn.update()
wn.mainloop()

