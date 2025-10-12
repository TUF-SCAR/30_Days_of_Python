print("Day 9 of Python - Conditionals")

print("\n", "-" * 25, "\n")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive!")

else:
    print(f"You need {18 - age} more years to learn to drive!")

print("\n\n")

my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:

    diff = your_age - my_age

    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")

elif your_age < my_age:

    diff = my_age - your_age

    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")

else:
    print("We are the same age.")

print("\n\n")

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print("Both are the same.")

print("\n", "-" * 25, "\n")

score = int(input("Enter your score: "))

if 0 <= score <= 100:

    if score <= 49:
        print("Your grade is F.")

    elif score <= 59:
        print("Your grade is D.")

    elif score <= 69:
        print("Your grade is C.")

    elif score <= 79:
        print("Your grade is B.")

    elif score <= 89:
        print("Your grade is A.")

    else:
        print("Your grade is A+.")

else:
    print("Invalid score!!")

print("\n\n")

autumn = {'september', 'sept', 'october', 'oct', 'november', 'nov'}
winter = {'december', 'dec', 'january', 'jan', 'february', 'feb'}
spring = {'march', 'mar', 'april', 'apr', 'may'}
summer = {'june', 'jun', 'july', 'jul', 'august', 'aug'}
month = input("Enter current month: ")
month.lower()

if month in autumn:
    print("Current Season: Autumn")
elif month in winter:
    print("Current Season: Winter")
elif month in spring:
    print("Current Season: Spring")
elif month in summer:
    print("Current Season: Summer")
else:
    print("Invalid month!")

print("\n\n")

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
user_fruit = input("Enter a fruit to add: ")

if user_fruit not in fruits:
    fruits.append(user_fruit)
else:
    print("That fruit already exists in the list!")

print("\n", "-" * 25, "\n")

person = {
    'first_name': 'Zoro',
    'last_name': 'Roronoa',
    'age': 25,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

skills = person['skills']
middle_index = len(skills) / 2
married = person['is_married']
country = person['country']


if 'skills' in person:

    print(f"Middle skill: {skills[middle_index]}")

    if 'Python' in skills:
        print(f"{person['first_name']} has Python skill")
    else:
        print(f"{person['first_name']} does not have Pyton skill")

    if ['JavaScript', 'React'] in skills:
        print("He is a front end developer")

    elif ['Node', 'Python', 'MongoDB']:
        print("He is a backend developer")

    elif ['React', 'Node', 'MongoDB']:
        print("He is a fullstack developer")

    else:
        print("Unknown Title")

if married and country == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in {country}. He is married.")

print("\n", "-" * 25, "\n")
