from math import pi
from math import sqrt

print("Day 3 of Python - Operators")

print("\n", "-" * 25, "\n")

my_age = 17
my_height = 180.5
complex_num = 10 - 6j

print("Triangle Area & Perimeter:- \n")

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("\tArea of triangle : ", area_of_triangle, '\n\n')

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = (side_a + side_b + side_c)
print("\tPerimeter of triangle : ", perimeter_of_triangle)

print("\n", "-" * 25, "\n")

print("Rectangle Area & Perimeter:- \n")

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("\tArea of rectangle : ", area_of_rectangle)
print("\tPerimeter of rectangle : ", perimeter_of_rectangle)

print("\n", "-" * 25, "\n")

print("Circle Area & Circumference:- \n")

radius = float(input("Enter radius: "))
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius
print("\tArea of circle : ", area_of_circle)
print("\tCircumference of circle : ", circumference_of_circle)

print("\n", "-" * 25, "\n")

print("Slope:- \n")
# y = 2x - 2

# slope (coefficient of x)
slope = 2
print("Slope of the line:", slope)

# y-intercept (put x = 0)
y_intercept = -2
print("Y-intercept: (0, -2)")

# x-intercept (put y = 0 -> 0 = 2x - 2)
x_intercept = 1
print("X-intercept: (1, 0)")

# Points
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_point = (y2 - y1) / (x2 - x1)
print("Slope between points : ", slope_point)

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance between points:", distance)

print("First slope == Second slope : ", slope == slope_point)

print("\n", "-" * 25, "\n")

print("Qudratic:- \n")

# y = x^2 + 6x + 9
a = 1
b = 6
c = 9
discriminant = b**2 - 4*a*c

if discriminant > 0:
    x_1 = (-b + sqrt(discriminant)) / 2 * a
    x_2 = (-b - sqrt(discriminant)) / 2 * a
    print(f"Root 1: {x_1}, Root 2: {x_2}")

elif discriminant == 0:
    x = -b / 2 * a
    print(f"if y = 0 then x = {x}")

else:
    print("No roots")

print("\n", "-" * 25, "\n")

print("length of 'python': ", len("python"))
print("length of 'dragon': ", len("dragon"))
print("len('python') != len('dragon') : ",
      len('python') != len('dragon'), '\n')

print(" 'on' found in 'python' and 'dragon' : ",
      'on' in 'python' and 'on' in 'dragon')

print(" 'jargon' in 'I hope this course is not full of jargon' : ",
      'jargon' in 'I hope this course is not full of jargon')
