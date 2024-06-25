#Kevin Sleem
#June 25, 2024
#P2LAB1
#Calculates Dimensions of a Circle

#import math module to use the constant, math.pi
import math
#get the radius from the user

radius = float(input('What is the radius of the circle? '))
print()
#calculate the diameter
diameter = 2 * radius
circumference = 2 * radius * math.pi
area = math.pi * radius**2
#Display the output
print(f'The diameter of the circle is {diameter:.1f}\n')
print(f'The circumference of the circle is {circumference:.2f}\n')
print(f'The area of the circle is {area:.3f}\n')
