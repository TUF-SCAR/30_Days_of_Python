print("Day 4 of Python - Strings")

print("\n", "-" * 25, "\n")

space = " "
a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
var1 = a + space + b + space + c + space + d

e = "Coding"
f = "For"
g = "All"
var2 = e + space + f + space + g

print("String 1 : ", var1)
print("String 2 : ", var2)

print("\n", "-" * 25, "\n")

company = "Coding foR aLl"

print("Initial string: ", company)
print("Length: ", len(company))
print("Upper: ", company.upper())
print("Lower: ", company.lower())
print("Capitalize: ", company.capitalize())
print("Title: ", company.title())
print("Case swap: ", company.swapcase())

cut = company[0:6]
print("Slice: ", cut)
print("Contains 'Coding' at: ", company.find('Coding'))
print("Replace: ", company.replace('Coding', 'Python'))
print("Replace: ", "Python for Everyone".replace('Everyone', 'All'))

split_space = company.split()
print("Split: ", split_space)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_comma = companies.split(', ')
print("Split: ", split_comma)
print("Index 1: ", company[0])
print("Last index: ", company[11])
print("Index 10: ", company[10])
print("PFE : ", 'Python For Everyone')
print("CFA : ", 'Coding For All')

company = "Coding For All"
print("'C' at: ", company.index('C'))
print("'F' at: ", company.index('F'))
print("'l' at: ", company.rfind('l'))

print("\n", "-" * 25, "\n")

sentence1 = """You cannot end a sentence with because because because is a conjunction"""
slice_sentence = sentence1.replace('because', ' ')

print("Because at: ", sentence1.find('because'))
print("Because at: ", sentence1.rfind('because'))
print("No Because: ", slice_sentence)
print("Start with 'Coding': ", company.startswith('Coding'))
print("End with 'coding': ", company.endswith('coding'))

var = '   Coding For All      '
print("Strip: ", var.strip())

var3 = '30DaysOfPython'
var4 = 'thirty_days_of_python'

print("Can be variable name?")
print("'30DaysOfPython' : ", var3.isidentifier())
print("'thirty_days_of_python' : ", var4.isidentifier())

print("\n", "-" * 25, "\n")

py_lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
py_lib = "# ".join(py_lib_list)

print("I am enjoying this challenge.\nI just wonder what is next.\n")

print("Name\tAge\tCountry\tCity")
print("Scar\t17\tIndia\tShandora")

print("\n", "-" * 25, "\n")

r = 10
pi = 3.14
area = pi * r ** 2
print(f"Radius = {r}")
print(f"Area = {pi} * {r} ** 2")
print(f"The area of a circle with radius {r} is {int(area)} meters square.")

print("\n", "-" * 25, "\n")

x = 8
y = 6

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} % {y} = {x % y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} ** {y} = {x ** y}")

print("\n", "-" * 25, "\n")
