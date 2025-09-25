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


print("\n", "-" * 25, "\n")
