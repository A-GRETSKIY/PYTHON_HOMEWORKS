# Homework 1
# Exercise 1. Write a Python-script that displays the message “Hello world”.
# Exercise 2. Rewrite the first script to display three any messages.
# Exercise 3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.
# Exercise 4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.
# Exercise 5. Write a program that reads in the radius of a circle and prints the circle’s diameter, circumference and area. Use the constant value 3.14159 for π. Do these calculations in output statements.

print('Hello world')

###

print('Glory to Ukraine\nJust do it!\nRed Bull Gives You Wings')

###

a = input('A=')
b = input('B=')
res = float(a) * float(b)
print('a * b =', res)

###

c = float(input('c='))
d = float(input('d='))
res = c + d
print('c + d=', res)
res = c - d
print('c - d=', res)
res = c * d
print('c * d=', res)
res = c / d
print('c / d=', res)

###

import math
r = float(input('Radius='))
res = r*2
print('Diametr:', 'r*2=', res)
res = 2 * math.pi * r
print('Circumference:', '2 * math.pi * r=', res)
res = math.pi*((r**2))
print('Area:', 'math.pi*(r**2)=', res)
