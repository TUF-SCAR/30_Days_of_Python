print("Day 6 of Python - Tuples")

print("\n", "-" * 25, "\n")

empty_tp = ()
print("Empty tuple: ", empty_tp, '\n')
# we will take Tanjiro from demon slayer as example
brothers = ('Takeo', 'Shigeru', 'Rokuta')
sisters = ('Nezuko', 'Hanako')
print("Brothers: ", brothers)
print("Sisters: ", sisters, '\n')
siblings = brothers + sisters
print("Siblings: ", siblings)
print("No of Siblings: ", len(siblings), '\n')
family_members = siblings + ('Kie', 'Tanjuro')
print("Family Members: ", family_members)

print("\n", "-" * 25, "\n")

siblings = family_members[:5]
parents = family_members[5:]
print("Siblings: ", siblings)
print("Parents: ", parents, '\n\n')

fruits = ('Apple', 'Banana', 'Mango')
vegetables = ('Onion', 'Potato', 'Cucumber')
animal_products = ('Chicken', 'Milk', 'Crab')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

print("Fruits: ", fruits)
print("Vegetables: ", vegetables)
print("Animal Products: ", animal_products)
print("Food Stuff Tuple: ", food_stuff_tp)
print("Food Stuff List: ", food_stuff_lt, '\n')

food_stuff_tp = food_stuff_tp[:4] + food_stuff_tp[5:]
print("No middle: ", food_stuff_tp, '\n')

food_stuff_lt = food_stuff_lt[3:]
food_stuff_lt = food_stuff_lt[:3]
print("No first and last three: ", food_stuff_lt, '\n')

del food_stuff_tp
# print("Food Stuff Tuple: ", food_stuff_tp) \\ it will give error that food_stuff_tp does not exist

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is Estonia a nordic country? : ", 'Estonia' in nordic_countries)
print("Is Iceland a nordic country? : ", 'Iceland' in nordic_countries)

print("\n", "-" * 25, "\n")
