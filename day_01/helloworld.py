from math import sqrt

print("Day 1 of Python - Hello, World!")

print("\n", "-" * 25, "\n")

print(3 + 4)  # Addition
print(3 - 4)  # Subtraction
print(3 * 4)  # Multiplication
print(3 % 4)  # Modulus (gives the reminder of the division)
print(3 / 4)  # Division
print(3 ** 4)  # Exponential
print(3 // 4)  # Floor Division

print("\n", "-" * 25, "\n")

print("First Name : Scar")
print("Last Name : TUF")
print("Country : India")
print("I am Enjoying 30 days of python!!! Really!!!")

print("\n", "-" * 25, "\n")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Scar', 'Python', 'India']))
print(type('Scar'))
print(type('TUF'))
print(type('India'))

print("\n", "-" * 25, "\n")

# Examples of different Python Data Types

print("Number:- ")
# An Integer can be any number without a decimal point or a exponent
print("\t Integer : ", 106)

print("\t Float : ", 3.14159)  # A Float is any number with a decimal point

# Complex is any expression with real and imaginary numbers
print("\t Complex : ", 6 - 9j)

# String is a collection of words
print("\nString: ", "Python is fun to learn!!\n")

# Boolean is a data type with only two values True or False
print("Boolean: ", True, '\n')

# List is a data type used to store ordered collection of items, it is mutable
print("List: ", [40, 102.35, False,
      'This is a List of different data types'], '\n')

# A Tuple is also like List but it is immutable, A Tuple of anime characters:-
print("Tuple: ", ('Naruto', 'Sasuke', 'Kakashi', 'Madara', 'Zoro'), '\n')

# A Set is a collection of unordered items and it is immutable
print("Set: ", {3.14159, 9.8, 2.71}, '\n')

# A Dictionary is a data structure which stores key-value pair and they are mutable and ordered
print("Dictionary: ", {
    'Date': '18/09/25',
    'Day': 'Thursday',
    'Year': 2025,
}, '\n')

print("\n", "-" * 25, "\n")

# Finding Euclidian distance between two points
# Two points A = (2, 3) and B = (10, 8)
# Let's take A = (a1, a2) and B = (b1, b2) for easier expression
# So a1 = 2, a2 = 3, b1 = 10, b2 = 8.

a1, a2 = 2, 3
b1, b2 = 10, 8

distance = sqrt((a1 - b1) ** 2 + (a2 - b2) ** 2)  # √( (2 - 10)² + (3 - 8)² )

print("Distance between points A(2, 3) and B(10, 8) : ", distance)

print("\n", "-" * 25, "\n")
