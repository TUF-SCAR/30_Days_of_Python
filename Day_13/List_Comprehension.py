print("Day 13 of Python - List Comprehension")

print("\n", "-" * 25, "\n")

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_numbers = [i for i in numbers if i <= 0]
print(f"Numbers: {filter_numbers}")

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
filter_list = [i for k in list_of_lists for j in k for i in j]
print(f"List: {filter_list}")

print("\n", "-" * 25, "\n")

result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(f"Result: {result}")

print("\n", "-" * 25, "\n")

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
new_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(f"New Countries: {new_countries}")

print("\n", "-" * 25, "\n")

dict_countries = [{"country": country, "city": city} for [(country, city)] in countries]
print(f"Dict Countries: {dict_countries}")

print("\n", "-" * 25, "\n")

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
full_names = [f"{first_name} {last_name}" for [(first_name, last_name)] in names]
print(f"Full Names: {full_names}")

print("\n", "-" * 25, "\n")

print("Slope:-\n")
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)

print(f"\nSlope: {slope(x1, x2, y1, y2)}\n\n")

print("Y Intercept:-\n")
x = float(input("Enter x: "))
y = float(input("Enter y: "))
m = float(input("Enter m: "))

y_intercept = lambda x, y, m: y - m * x

print(f"\nY Intercept: {y_intercept(x, y, m)}")

print("\n", "-" * 25, "\n")
