from import_modules import *

print("Day 12 of Python - Modules")

print("\n", "-" * 25, "\n")

print(f"Random_user_id : {random_user_id()}", '\n')
user_id_gen_by_user()
rgb_color_gen()

print("\n", "-" * 25, "\n")

print(f"Hexa color: {list_of_hexa_colors()}\n")
print(f"RGB: {list_of_rgb_colors()}\n")

x = input("Enter mode (hexa/rgb): ")
y = int(input("No of colors: "))
print(generate_colors(x, y), '\n')

print("\n", "-" * 25, "\n")

lst = ['Naruto', 'Luffy', 'Zoro', 'Sasuke', 'Sanji',
       'Sakura', 'Nami', 'Kakashi', 'Shanks', 'Itachi']
print(f"Before shuffle: {lst}")
print(f"After shuffle: {shuffle_list(lst)}\n")
print("Unique random numbers:-")
seven_random_numbers()

print("\n", "-" * 25, "\n")
