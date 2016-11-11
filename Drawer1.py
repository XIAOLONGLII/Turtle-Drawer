"""
Katherine St. John, Spring 2015
Introductory Programming, Lehman College, CUNY
Read colors from a file and display using turtle graphics
"""

from turtle import *

""" Welcome messages for the program"""
def welcome():
    print("This program prints pixelated pictures")
    print("stored as lists of colors in text files.")
    print()

""" Sets up the screen with the origin in upper left corner """
def setUpScreen(xMax,yMax):
    win = Screen()
    win.setworldcoordinates(-0.5, yMax+0.5,xMax+0.5,-0.5)
    return win

""" Draws a grid to the graphics window"""
def drawGrid(xMax,yMax):
    tic = Turtle()
    tic.speed(10)
    #Draw the vertical bars of the game board:
    for i in range(0,xMax+1):
        tic.up()
        tic.goto(0,i)
        tic.down()
        tic.forward(yMax)

    #Draw the horizontal bars of the game board:
    tic.left(90)    #Point the turtle in the right direction before drawing
    for i in range(0,yMax+1):
        tic.up()
        tic.goto(i,0)
        tic.down()
        tic.forward(xMax)

""" Fills in the square (x,y) with color"""
def fillSquare(x,y,color):
    t = Turtle()
    t.hideturtle()  #Hides cursor and speeds up drawing
    t.speed(10)
    t.up()
    t.goto(x,y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(1)
        t.left(90)
    t.end_fill()

""" Ask user for input file and return the file handler, lines, height and width"""
def getData():
    fname = input('Enter file name: ')
    infile = open(fname, "r")
    lines = infile.readlines()
    infile.close()
    height = len(lines)
    width = lines[0].count(" ")+1
    print(height, width)
    return lines, height, width



"""Draws the colors to the graphics window:"""
def drawColors(lines):
    #For each row in the file:
    for row in range(len(lines)):
        #Break the row into pieces (stripping off any trailing newlines or spaces)
        cells = lines[row].rstrip().split(" ")
        #For each entry, fill in with the specified color:
        for column in range(len(cells)):
            fillSquare(column,row,cells[column])

            
def main():
    welcome()
    lines, m, n = getData()
    win = setUpScreen(m,n)
    drawGrid(m,n)
    drawColors(lines)
    win.exitonclick()       #Close window when mouse is clicked
main()
