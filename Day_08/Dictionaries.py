print("Day 8 of Python - Dictionaries")

print("\n", "-" * 25, "\n")

dog = dict()

print("Empty Dictionary: ", dog, '\n')

dog['name'] = 'Chopper'  # :)
dog['color'] = 'Brown'
dog['breed'] = 'Reindeer'
dog['legs'] = 4
dog['age'] = 10

print("Dog: ", dog, '\n')

student = {
    'first_name': 'Zoro',
    'last_name': 'Roronoa',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'NO',
    'skills': ['Three Swords Style', 'Sleeping', 'Getting Lost'],
    'country': 'Japan',
    'city': 'Wano',
    'address': '11-11, 2nd Street, The Flower Capital, Wano'
}

print("Student: ", student, '\n')
print("Length: ", len(student), '\n')
print("Skills: ", student['skills'], '\n')
print("Type: ", type(student['skills']), '\n')
student['skills'].append('Drinking')
print("Student: ", student, '\n')
keys = student.keys()
values = student.values()
print("Keys: ", keys, '\n')
print("Values: ", values, '\n')
student['marital_status'] = ''
print("Student: ", student, '\n')
student.pop('marital_status')
print("Student: ", student)

print("\n", "-" * 25, "\n")
