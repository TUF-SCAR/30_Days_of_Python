import country_list

print("Day 5 of Python - Lists")

print("\n", "-" * 25, "\n")

emp_list = []
lst = ["Naruto", "Sasuke", "Luffy", "Zoro", "Sanji"]
print("Empty list: ", emp_list)
print("List: ", lst)
print("List length: ", len(lst))
print("First: ", lst[0])
print("Middle: ", lst[2])
print("Last: ", lst[4])

print("\n", "-" * 25, "\n")

mixed_data_types = ["Scar", 17, 5.5, False, {
    'country': 'India', 'city': 'Shandora'}]
print("List with different data types: ", mixed_data_types)
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
print("IT Companies: ", it_companies)
print("No of IT Companies: ", len(it_companies))
print("First: ", it_companies[0])
print("Middle: ", it_companies[3])
print("Last: ", it_companies[6])
it_companies[5] = 'Dell'
print("List: ", it_companies)
it_companies.append('Intel')
print("List: ", it_companies)
it_companies.insert(4, 'TCS')
print("List: ", it_companies)
it_companies[3] = it_companies[3].upper()
print("List: ", it_companies)
joined_companies = '#; '.join(it_companies)
print("Joined List: ", joined_companies)
print("Google in List: ", 'Google' in it_companies)
it_companies.sort()
print("Sorted List: ", it_companies)
it_companies.reverse()
print("Reverse List: ", it_companies)
slice_it_companies = it_companies[4:9]
print("Slice 1: ", slice_it_companies)
slice_it_companies = it_companies[0:5]
print("Slice 2: ", slice_it_companies)
slice_it_companies = it_companies[0:4] + it_companies[5:9]
print("Slice 3: ", slice_it_companies)
it_companies.pop(0)
print("List: ", it_companies)
it_companies.pop(7)
print("List: ", it_companies)
it_companies.pop(3)
print("List: ", it_companies)
it_companies.clear()
print("List: ", it_companies)
del it_companies
# print("List: ", it_companies) \\ It will give a error that it_companies does not exist

print("\n", "-" * 25, "\n")

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
print("Front End: ", front_end)
print("Back End: ", back_end)
front_end.extend(back_end)
print("ALL: ", front_end)
full_stack = front_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print("Full Stack: ", full_stack)

print("\n", "-" * 25, "\n")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Ages: ", ages)
ages.sort()
print("Ages: ", ages)
print("Min Age: ", min(ages))
print("Max Age: ", max(ages))

n = len(ages)

if n % 2 == 0:
    mid1 = ages[n//2-1]
    mid2 = ages[n//2]
    median = (mid1 + mid2) / 2
else:
    median = ages[n//2]

avg_age = sum(ages)/len(ages)
min_age = min(ages)
max_age = max(ages)

print("Median Age: ", median)
print("Average Age: ", avg_age)
print("Range Age: ", max_age - min_age)

diff_min = abs(min_age - avg_age)
diff_max = abs(max_age - avg_age)

print("Min Age: ", min_age)
print("Max Age: ", max_age)
print("Average Age: ", avg_age)
print("abs(min - avg): ", diff_min)
print("abs(max - avg): ", diff_max)

print("\n", "-" * 25, "\n")

country = country_list.countries
length = len(country)

if length % 2 == 0:
    middle_country = [country[(length // 2) - 1], country[length // 2]]
    half1 = country[:length//2]
    half2 = country[length//2:]
else:
    middle_country = country[length // 2]
    half1 = country[:length//2 + 1]
    half2 = country[length//2 + 1:]

print("Countries : ", country)

print("\n", "-" * 25, "\n")

print("Middle country: ", middle_country, '\n\n')

print("First Half: ", half1)

print("\n", "-" * 25, "\n")

print("Second Half: ", half2)

print("\n", "-" * 25, "\n")

a, b, c, *scandic = ['China', 'Russia', 'USA',
                     'Finland', 'Sweden', 'Norway', 'Denmark']

print(f"First Three:\t{a}\t{b}\t{c}")
print("Scandic: ", scandic)

print("\n", "-" * 25, "\n")
