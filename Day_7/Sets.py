print("Day 7 of Python - Sets")

print("\n", "-" * 25, "\n")

it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
extra_companies = ['Nividia', 'Intel', 'AMD', 'Samsung']

print("IT Companies: ", it_companies)
print("Length: ", len(it_companies))
it_companies.add('Twitter')
print("IT Companies: ", it_companies)
it_companies.update(extra_companies)
print("IT Companies: ", it_companies)
remove = it_companies.pop()
print("Removed: ", remove)
print("IT Companies: ", it_companies)

# discard() - removes the item and if it doesn't exist in the set it will not give error
# remove() - same as discard but it will give error

print("\n", "-" * 25, "\n")

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print("A: ", A)
print("B: ", B)
print("C: ", C)
print("A intersection B: ", A.intersection(B))
print("A and B disjoint? : ", A.isdisjoint(B))
AB = A.union(B)
BA = B.union(A)
print("AB: ", AB)
print("BA: ", BA)
print("A and B symmetric difference: ", A.symmetric_difference(B))
del A
del B
del C
del AB
del BA

# These will not work because we have deleted all the sets
# It will give error that the set does not exist

# print("A: ", A)
# print("B: ", B)
# print("C: ", C)
# AB = A.union(B)
# BA = B.union(A)

print("\n", "-" * 25, "\n")

age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)
print("age list length: ", len(age))
print("age set length: ", len(age_set))

print('\n\n')

print(f"{'Type':<10} {'Syntax Example':<20} {'Mutable?':<12} {'Ordered?':<10} {'Allows Duplicates?':<18} {'Key Use':<30}")
print("-" * 110)
print(f"{'String':<10} {'\'Hello\'':<20} {'No':<12} {'Yes':<10} {'Yes':<18} {'Store text':<30}")
print(
    f"{'List':<10} {'[1, 2, 3]':<20} {'Yes':<12} {'Yes':<10} {'Yes':<18} {'Store multiple items (editable)':<30}")
print(f"{'Tuple':<10} {'(1, 2, 3)':<20} {'No':<12} {'Yes':<10} {'Yes':<18} {'Fixed collection of items':<30}")
print(f"{'Set':<10} {'{1, 2, 3}':<20} {'Yes':<12} {'No':<10} {'No':<18} {'Unique unordered collection':<30}")

print('\n\n')

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Unique words: ", unique_words)
print("No of Unique words: ", len(unique_words))

print("\n", "-" * 25, "\n")
