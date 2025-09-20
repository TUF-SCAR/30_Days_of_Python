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

print("Quadratic:- \n")

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

print("There is no 'on' in 'dragon' and 'python': ",
      'on' not in 'dragon' and 'on' not in 'python')

len_of_python = len('python')
float_len = float(len_of_python)
string_float = str(float_len)
print("\tLength of 'python': ", len_of_python)
print("\tin float: ", float_len)
print("\tfloat in string: ", string_float)

print("\n", "-" * 25, "\n")

check_even = int(input("Enter a number to check: "))

if check_even % 2 == 0:
    print(f"{check_even} is even")
else:
    print(f"{check_even} is not even")

print("7 // 3 == int(2.7): ", 7 // 3 == int(2.7))
print("'10' == 10: ", '10' == 10)

# we can't convert '9.8' into int because it is not a integer string
# so we convert it to float then int
print("int('9.8') == 10: ", int(float('9.8')) == 10)

print("\n", "-" * 25, "\n")

hours_of_work = int(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours_of_work * rate_per_hour
print("Weekly pay: ", pay, '\n')

years_lived = int(input("Enter number of years you have lived: "))
days_lived = years_lived * 356
hours_lived = days_lived * 24
minutes_lived = hours_lived * 60
seconds_lived = minutes_lived * 60
print("You have lived:- ")
print(f"{days_lived} days \t\tor")
print(f"{hours_lived} hours \t\tor")
print(f"{minutes_lived} minutes \tor")
print(f"{seconds_lived} seconds")

print("\n", "-" * 25, "\n")

for i in range(1, 6):
    a = 1 * i
    b = a * i
    c = b * i
    print(f"{i}\t1\t{a}\t{b}\t{c}")

print("\n", "-" * 25, "\n")
