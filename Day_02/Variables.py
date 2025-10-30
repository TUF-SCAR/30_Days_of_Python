from math import pi

print("Day 2 of Python - Variables")

print("\n", "-" * 25, "\n")

first_name = "Scar"
last_name = "TUF"
full_name = last_name + '_' + first_name
country = "India"
city = "Shandora"
age = 17
year = 2025
is_married = False  # No :(
is_true = True
is_light_on = False
a, b, c = 1, 2, 3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

print("\n", "-" * 25, "\n")

print(len(first_name), '\n')
print(len(first_name) == len(last_name), '\n')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("1st num: ", num_one)
print("2nd num: ", num_two)
print("total: ", total)
print("difference: ", diff)
print("product: ", product)
print("division: ", division)
print("remainder: ", remainder)
print("power: ", exp)
print("Floor Division: ", floor_division)

print("\n", "-" * 25, "\n")

radius = 30
area_of_circle = pi * (radius ** 2)
circumference_of_circle = 2 * pi * radius

print(f"Area and Circumference of a circle with radius ({radius}):-")
print(f"Area: {area_of_circle}, Circumference: {circumference_of_circle}")

user_radius = int(input("Enter Circle Radius: "))
user_area_of_circle = pi * (user_radius ** 2)
user_circumference_of_circle = 2 * pi * user_radius

print(f"Area and Circumference of a circle with radius ({user_radius}):-")
print(
    f"Area: {user_area_of_circle}, Circumference: {user_circumference_of_circle}")

print("\n", "-" * 25, "\n")

user_first_name = input("Enter Your First Name: ")
user_last_name = input("Enter Your Last Name: ")
user_country = input("Enter Your Country: ")
user_age = int(input("Enter Your Age: "))

print("Your First Name: ", user_first_name)
print("Your Last Name: ", user_last_name)
print("Your Country: ", user_country)
print("Your Age: ", user_age)

print("\n", "-" * 25, "\n")
