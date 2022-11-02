# Emanuel Ramos
#
# 11/1/2022
#
# Description: draws a triangle or a square using the inputs of the user and for loops

import turtle
Object = turtle.Turtle()

length = int(input("What is the length of the sides?"))
color = input("What color do you want the object to be filled with?")
shape = int(input("""What shape would you like to make?
1. Triangle
2. Square\n"""))

if shape == 1:
    Object.fillcolor(color)
    Object.begin_fill()
    for triangle in range(3):
        Object.forward(length)
        Object.left(120)
    Object.end_fill()

else:
    Object.fillcolor(color)
    Object.begin_fill()
    for square in range(4):
        Object.forward(length)
        Object.left(90)
    Object.end_fill()
input()
