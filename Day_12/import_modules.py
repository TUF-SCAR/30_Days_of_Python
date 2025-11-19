import string
from random import *


def random_user_id():
    str_characters = string.ascii_letters + string.digits
    str_id = ''
    for i in range(6):
        str_id += choice(str_characters)
    return str_id


def user_id_gen_by_user():
    str_characters = string.ascii_letters + string.digits
    str_id = ''
    print("User input:-")
    no_of_char = int(input("No of characters: "))
    no_of_ids = int(input("No of id's: "))
    for i in range(no_of_ids):
        for j in range(no_of_char):
            str_id += choice(str_characters)
        print(f"User_id {i + 1} : {str_id}")
        str_id = ''
    print('\n')


def rgb_color_gen():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    print(f"rgb({R}, {G}, {B})", '\n')


def list_of_hexa_colors():
    hexa_symbols = 'abcdef' + string.digits
    hexa_color = ''
    array = []
    no_of_colors = int(input("No of colours: "))
    for i in range(no_of_colors):
        for i in range(6):
            hexa_color += choice(hexa_symbols)
        array.append(f"#{hexa_color}")
        hexa_color = ''
    return array


def list_of_rgb_colors():
    no_of_colors = int(input("No of colours: "))
    array = []
    for i in range(no_of_colors):
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)
        array.append(f"rgb({R}, {G}, {B})")
    return array


def generate_colors(mode, no_of_colors):
    if mode == 'hexa':
        hexa_symbols = 'abcdef' + string.digits
        hexa_color = ''
        array = []
        for i in range(no_of_colors):
            for i in range(6):
                hexa_color += choice(hexa_symbols)
            array.append(f"#{hexa_color}")
            hexa_color = ''
        return 'Hexa color: ' + str(array)
    elif mode == 'rgb':
        array = []
        for i in range(no_of_colors):
            R = randint(0, 255)
            G = randint(0, 255)
            B = randint(0, 255)
            array.append(f"rgb({R}, {G}, {B})")
        return 'RGB: ' + str(array)
    else:
        error = "Incorrect mode - hexa / rgb only"
        return error


def shuffle_list(in_list):
    shuffled_list = list()
    while (len(in_list) != 0):
        index = randint(0, len(in_list) - 1)
        temp = in_list[index]
        in_list.pop(index)
        shuffled_list.append(temp)
    return shuffled_list


def seven_random_numbers():
    num = set()
    while (len(num) != 7):
        num.add(randint(0, 9))
    print(f"Number: {list(num)}", '\n')
