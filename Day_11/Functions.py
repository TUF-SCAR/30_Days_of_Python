from math import pi, sqrt
from keyword import iskeyword
from collections import Counter
from country_info import country_info


def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


def area_of_circle(radius):
    area = pi * radius * radius
    return area


def add_all_nums(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            return "All arguments must be numbers!"
    return sum(args)


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def check_season(month):
    autumn = {'september', 'sept', 'october', 'oct', 'november', 'nov'}
    winter = {'december', 'dec', 'january', 'jan', 'february', 'feb'}
    spring = {'march', 'mar', 'april', 'apr', 'may'}
    summer = {'june', 'jun', 'july', 'jul', 'august', 'aug'}
    month.lower()

    if month in autumn:
        return "Current Season: Autumn"
    elif month in winter:
        return "Current Season: Winter"
    elif month in spring:
        return "Current Season: Spring"
    elif month in summer:
        return "Current Season: Summer"
    else:
        return "Invalid month!"


def calculate_slope():
    print("Enter the points on the line:-")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    m = (y2 - y1) / (x2 - x1)
    print("Slope : ", m)


def solve_quadratic_eqn():
    print("Enter the value to solve quadratic equation:-")
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))
    d = (b * b) - (4 * a * c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("The roots of the quadratic equation are:-")
        print(f"x = {x1} or x = {x2}")

    elif d == 0:
        x = -b / (2 * a)
        print("The root of the quadratic equation is:-")
        print(f"x = {x}")

    else:
        print("There are no real roots of the quadratic equation.")


def print_list(in_list):
    for item in in_list:
        print(item)


def reverse_list(array):
    reversed_list = []
    for i in range(len(array) - 1, -1, -1):
        reversed_list.append(array[i])
    return reversed_list


def capitalize_list_items(items):
    capitalized = []
    for item in items:
        capitalized.append(item.capitalize())
    return capitalized


def add_item(in_list, item):
    in_list.append(item)
    return in_list


def remove_item(in_list, item):
    in_list.remove(item)
    return in_list


def sum_of_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total


def sum_of_even(num):
    total = 0
    for i in range(0, num + 1, 2):
        total += i
    return total


def evens_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The no of odds are {odds}")
    print(f"The no of evens are {evens}")


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


def is_empty(item):
    if item:
        return False
    else:
        return True


def calculate_mean(num):
    total = sum(num)
    count = len(num)
    mean = total / count
    return mean


def calculate_median(num):
    num.sort()
    n = len(num)
    mid = n // 2

    if n % 2 == 0:
        median = (num[mid - 1] + num[mid]) / 2
    else:
        median = num[mid]
    return median


def calculate_mode(num):
    frequency = {}
    for n in num:
        frequency[n] = frequency.get(n, 0) + 1
    max_count = max(frequency.values())
    mode = [n for n, count in frequency.items() if count == max_count]
    return mode


def calculate_range(num):
    return max(num) - min(num)


def calculate_variance(num):
    mean = calculate_mean(num)
    squared_diff = [(x - mean) ** 2 for x in num]
    variance = sum(squared_diff) / len(num)
    return variance


def calculate_std(num):
    variance = calculate_variance(num)
    std = sqrt(variance)
    return std


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_unique(in_list):
    if len(in_list) == len(set(in_list)):
        return True
    else:
        return False


def same_data_type(in_list):
    if not in_list:
        return True
    first_type = type(in_list[0])
    for item in in_list:
        if type(item) != first_type:
            return False
    return True


def is_valid_variable(var_name):
    if var_name.isidentifier() and not iskeyword(var_name):
        return True
    else:
        return False


def most_spoken_languages():
    languages = []
    for country in country_info:
        languages.extend(country['languages'])
    lang_count = Counter(languages)
    most_spoken = lang_count.most_common(20)
    print("Top 20 Most Spoken Languages:-", '\n')
    for lang, count in most_spoken:
        print(f"{lang}, spoken in {count} countries")


def most_populated_countries():
    sorted_by_population = sorted(
        country_info, key=lambda c: c['population'], reverse=True
    )
    print("Top 20 Most Populated Countries:-", '\n')
    for i in sorted_by_population[:20]:
        print(f"{i['name']}: {i['population']:,},")


if __name__ == "__main__":
    print("Day 11 of Python - Functions")

    print("\n", "-" * 25, "\n")

    print("Sum of two numbers:-")
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print(f"Sum of {a} and {b} is {add_two_numbers(a, b)}", '\n')

    print("Calculating area of circle:-")
    r = int(input("Enter radius of circle: "))
    print(f"Area of radius({r}): {area_of_circle(r)}", '\n')

    print("Sum of all numbers:-")
    print("Enter numbers separated by space:")
    nums = input("Numbers: ").split()
    nums = [float(x) for x in nums]
    print("Sum of all numbers:", add_all_nums(*nums), '\n')

    print("Converting celsius to fahrenheit:-")
    c = float(input("Enter celsius: "))
    print("In fahrenheit: ", convert_celsius_to_fahrenheit(c), '\n')

    print("Checking season:-")
    m = input("Enter month to check season: ")
    print("Season: ", check_season(m), '\n')

    calculate_slope()
    print('\n')

    solve_quadratic_eqn()
    print('\n')

    print("Enter a list for functions:-")
    print("Enter list items separated by space:")
    user_list = input("List: ").split()

    print("Printing items of list seperately:-")
    print("Your list:")
    print_list(user_list)
    print('\n')

    print("Reversing items in list:-")
    print("Reversed list: ", reverse_list(user_list), '\n')

    print("Capitalize items in list:-")
    print("Capitalized list: ", capitalize_list_items(user_list), '\n')

    print("Adding item to list:-")
    new_item = input("Enter item to add: ")
    print("After adding: ", add_item(user_list, new_item), '\n')

    print("Removing item from list:-")
    delete_item = input("Enter item to remove: ")
    print("After removing: ", remove_item(user_list, delete_item), '\n')

    print("Sum of numbers:-")
    n = int(input("Enter a number to find sum of numbers: "))
    print("Sum:", sum_of_numbers(n), '\n')

    print("Sum of odds:-")
    n = int(input("Enter a number to find sum of odds: "))
    print("Sum of odds:", sum_of_odds(n), '\n')

    print("Sum of evens:-")
    n = int(input("Enter a number to find sum of evens: "))
    print("Sum of evens:", sum_of_even(n), '\n')

    print("\n", "-" * 25, "\n")

    print("Counting no of odds and evens:-")
    n = int(input("Enter a number to count evens and odds: "))
    evens_and_odds(n)
    print('\n')

    print("Factorial of number:-")
    n = int(input("Enter a number to find factorial: "))
    print("Factorial:", factorial(n), '\n')

    print("Checking if list is empty or not:-")
    print("Enter list items separated by space (or nothing for empty):")
    user_list = input("List: ").split()
    print("Is empty:", is_empty(user_list), '\n')

    print("Calculating mean:-")
    print("Enter numbers for mean (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Mean:", calculate_mean(nums), '\n')

    print("Calculating median:-")
    print("Enter numbers for median (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Median:", calculate_median(nums), '\n')

    print("Calculating mode:-")
    print("Enter numbers for mode (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Mode:", calculate_mode(nums), '\n')

    print("Calculating range:-")
    print("Enter numbers for range (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Range:", calculate_range(nums), '\n')

    print("Calculating variance:-")
    print("Enter numbers for variance (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Variance:", calculate_variance(nums), '\n')

    print("Calculating standard deviation:-")
    print("Enter numbers for standard deviation (space-separated):")
    nums = [float(x) for x in input().split()]
    print("Standard Deviation:", calculate_std(nums), '\n')

    print("\n", "-" * 25, "\n")

    print("Checking if number is prime:-")
    n = int(input("Enter a number to check if prime: "))
    print("Is prime:", is_prime(n), '\n')

    print("Checking if items in list are unique:-")
    print("Enter list items to check uniqueness (space-separated):")
    items = input().split()
    print("Is unique:", is_unique(items), '\n')

    print("Checking if the items in list are same data type:-")
    print("Enter list items (space-separated):")
    items = input().split()
    print("Same data type:", same_data_type(items), '\n')

    print("Checking if the name is valid variable name:-")
    var_name = input("Enter variable name to check validity: ")
    print("Valid variable:", is_valid_variable(var_name), '\n')

    print("Countries data:-")
    print("Most spoken languages:")
    most_spoken_languages()
    print('\n\n')

    print("Most populated countries:")
    most_populated_countries()

    print("\n", "-" * 25, "\n")
