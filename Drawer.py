#Walking Turtle program for Intro Programming Lab

import turtle
import random

def drawRing(t,radius,color):
    t.up()
    t.goto(0,-radius)
    t.color(color)
    t.down()
    t.circle(radius)

def setUpTurtle():
    #Create turtle
    t = turtle.Turtle()

    #Use the turtle to draw the rings:
    drawRing(t,100,"green")
    drawRing(t,200,"yellow")
    drawRing(t,300,"red")

    #Return turtle to starting position and set shape, speed, and color:
    t.up()
    t.home()
    t.down()
    t.color("purple")
    t.shape("turtle")
    t.speed(10)

    #Return turtle to used elsewhere in the program:
    return t

def main():
    tess = setUpTurtle()
    
    for steps in range(500):
        direction = random.random()
        if direction < 1/4:
            tess.right(90)
        elif direction < 1/2:
            tess.right(180)
        elif direction < 3/4:
            tess.left(90)
        tess.forward(10)

    turtle.Screen().exitonclick()

main()
