from collections import Counter
import country_file
import country_info

print("Day 10 of Python - Loops")

print("\n", "-" * 25, "\n")

for f in range(0, 11):
    print(f"for : {f}")

print()

w = 0
while w <= 10:
    print(f"while : {w}")
    w += 1

print()

for f in range(10, -1, -1):
    print(f"for : {f}")

print()

w = 10
while w >= 0:
    print(f"while : {w}")
    w -= 1

print("\n", "-" * 25, "\n")

for i in range(1, 8):
    print('*' * i)

print()

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

print()

for i in range(11):
    print(f"{i} * {i} = {i * i}")

print("\n", "-" * 25, "\n")

items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in items:
    print(item)

print()

for i in range(0, 101, 2):
    print(i, end=" ")

print()

for i in range(1, 101, 2):
    print(i, end=" ")

print("\n", "-" * 25, "\n")

sum = 0

for i in range(0, 101):
    sum += i

print(f"The sum of all numbers is {sum}", '\n')

odd_sum = 0
even_sum = 0

for i in range(0, 101, 2):
    odd_sum += i

for i in range(1, 101, 2):
    even_sum += i

print(f"The sum of all evens is {even_sum}.", end=" ")
print(f"And the sum of all odds is {odd_sum}.")

print("\n", "-" * 25, "\n")

countries = country_file.countries
land_countries = []

for country in countries:
    if 'land' in country:
        land_countries.append(country)

for country in land_countries:
    print(country)

print()

fruits = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

print("\n", "-" * 25, "\n")

country_data = country_info.country_info
languages = []

for country in country_data:
    languages.extend(country['languages'])

unique_languages = set(languages)
print(f"Total no of unique languages: {len(unique_languages)}")

print("\n")

lang_count = Counter(languages)
most_spoken = lang_count.most_common(10)

print("Top 10 Most Spoken Languages: ", "\n")

for lang, count in most_spoken:
    print(f"{lang}, spoken in {count} countries")

print("\n")

sorted_by_population = sorted(
    country_data, key=lambda c: c['population'], reverse=True
)

print("10 Most Populated Countries:", "\n")
for c in sorted_by_population[:10]:
    print(f"{c['name']}: {c['population']:,}")

print("\n", "-" * 25, "\n")
