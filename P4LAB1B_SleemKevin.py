#Kevin Sleem
#July 10, 2024
#P4LAB1B
#Initials, Draw InitiaLls Using Turtle Graphics

import turtle
win = turtle.Screen()
win.bgcolor('lightblue')
win.title('Draw Initials')

#Create Turtle Kevin Square
kevin = turtle.Turtle()
kevin.color('red')
kevin.pensize(3)

kevin.left(90)
kevin.forward(50)
kevin.left(180)
kevin.forward(25)
kevin.left(45)
kevin.forward(40)
kevin.left(180)
kevin.forward(40)
kevin.right(90)
kevin.forward(40)

kevin.penup()
kevin.right(45)
kevin.forward(80)
kevin.pendown()
kevin.left(180)
kevin.forward(30)
kevin.left(90)
kevin.forward(30)
kevin.left(90)
kevin.forward(30)
kevin.right(90)
kevin.forward(30)
kevin.right(90)
kevin.forward(30)


win.mainloop()
