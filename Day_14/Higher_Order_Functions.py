import countries_file
import countries_data_file
from functools import reduce

country_data = countries_data_file.country_data

print("Day 14 of Python - Higher Order Functions")

print("\n", "-" * 25, "\n")

sentence_1 = """1. Map is a function that applies a function to all elements.
2. Filter is a function that keep all elements which return true and leaves all elements which return false.
3. Reduce is a function that executes the function and give only one value. it returns only one value."""

sentence_2 = """1. Higher Order Functions are functions which take other functions as argument or returns a function.
2. Closure is a function that remembers variables from its outer functions.
3. Decorator is a function that is used to modify other function without changing the function source code."""

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
items = [1, "hello", 2, "python", 3.5, "world"]

print(sentence_1, "\n\n")
print(sentence_2, "\n")

print("\n", "-" * 25, "\n")


def change_to_upper(name):
    return name.upper()


def even(num):
    if num % 2 == 0:
        return True
    return False


def add_all(x, y):
    return int(x) + int(y)


upper_countries = map(change_to_upper, countries)
even_numbers = filter(even, numbers)
add_all_numbers = reduce(add_all, numbers)

print(list(upper_countries), "\n")
print(list(even_numbers), "\n")
print(add_all_numbers, "\n")

print("\n", "-" * 25, "\n")


def square(num):
    return num**2


def contain_land(country):
    if "land" in country:
        return True
    return False


def only_six(country):
    if len(country) == 6:
        return True
    return False


def more_than_six(country):
    if len(country) >= 6:
        return True
    return False


def has_e(country):
    if country.startswith("E"):
        return True
    return False


square_numbers = map(square, numbers)
upper_names = map(change_to_upper, names)
has_land = filter(contain_land, countries)
exactly_six = filter(only_six, countries)
more_six = filter(more_than_six, countries)
only_e = filter(has_e, countries)

print(list(square_numbers), "\n")
print(list(upper_names), "\n")
print(list(has_land), "\n")
print(list(exactly_six), "\n")
print(list(more_six), "\n")
print(list(only_e), "\n")

print("\n", "-" * 25, "\n")

result = reduce(
    lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers))
)

print(f"Result: {result}", "\n")


def get_string_only(lst):
    return list(filter(lambda x: isinstance(x, str), lst))


print(get_string_only(items), "\n")
print(add_all_numbers, "\n")

sentence = reduce(lambda a, b: a + ", " + b, countries).rsplit(", ", 1)
sentence = sentence[0] + ", and " + sentence[1] + " are North European countries"

print(sentence)


def categorize_countries(pattern):
    return list(
        filter(
            lambda country: pattern.lower() in country.lower(), countries_file.countries
        )
    )


print(categorize_countries("land"), "\n")
print(categorize_countries("ia"), "\n")
print(categorize_countries("island"), "\n")
print(categorize_countries("stan"), "\n")


def count_countries_by_starting_letter(countries=countries_file.countries):
    country_result = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in country_result:
            country_result[first_letter] += 1
        else:
            country_result[first_letter] = 1
    return country_result


def get_first_ten_countries(countries=countries_file.countries):
    return countries[:10]


def get_last_ten_countries(countries=countries_file.countries):
    return countries[-10:]


print(count_countries_by_starting_letter())
print(get_first_ten_countries())
print(get_last_ten_countries())

print("\n", "-" * 25, "\n")

countries_by_name = list(
    map(
        lambda country: country["name"],
        sorted(country_data, key=lambda country: country["name"]),
    )
)

print(countries_by_name)

print("\n", "-" * 25, "\n")

countries_by_capital = list(
    map(
        lambda country: country["name"],
        sorted(country_data, key=lambda country: country["capital"]),
    )
)

print(countries_by_capital)

print("\n", "-" * 25, "\n")

countries_by_population = list(
    map(
        lambda country: country["name"],
        sorted(country_data, key=lambda country: country["population"]),
    )
)

print(countries_by_population)

print("\n", "-" * 25, "\n")

language_count = {}

for country in country_data:
    for lang in country["languages"]:
        if lang in language_count:
            language_count[lang] += 1
        else:
            language_count[lang] = 1

sort_language = sorted(language_count.items(), key=lambda pair: pair[1], reverse=True)
top_ten_lang = sort_language[:10]

print(top_ten_lang)

print("\n", "-" * 25, "\n")

country_population = list(
    map(
        lambda country: country["name"],
        sorted(country_data, key=lambda country: country["population"], reverse=True),
    )
)

top_ten_population = country_population[:10]

print(top_ten_population)

print("\n", "-" * 25, "\n")
