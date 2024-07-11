#Kevin Sleem
#July 10, 2024
#P4LAB1A
#Shapes, draw a sqaure and triangle using Turtle Graphics

#Set up window and its attributes
import turtle
win = turtle.Screen()
win.bgcolor('orange')
win.title('Draw a Square and Triangle')

#Create Turtle Kevin Square
kevin = turtle.Turtle()
kevin.color('green')
kevin.pensize(3)

#Create Turtle Eddie Triangle
eddie = turtle.Turtle()
eddie.color('blue')
eddie.pensize(5)

#Draw square
kevin.forward(200)
kevin.left(90)
kevin.forward(200)
kevin.left(90)
kevin.forward(200)
kevin.left(90)
kevin.forward(200)

#Move Turtle away from origin
kevin.right(180)
kevin.forward(80)

#Draw triangle
for i in [0,1,2]:
    eddie.forward(60)
    eddie.left(120)

win.mainloop()

