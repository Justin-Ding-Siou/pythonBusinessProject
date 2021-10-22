
# Squared Integers using list comprehension

a_list = [1, '4', 9, 'a', 0, 4]

squared_ints = [ e**2 for e in a_list if type(e) == int ]

print (squared_ints)
# [ 1, 81, 0, 16 ]


# Dict Comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Double each value in the dictionary
double_dict1 = { k: v**2 for (k,v) in dict1.items() }
print(double_dict1)

double_key_dict = { k*2: v**2 for (k,v) in dict1.items() }
print(double_key_dict)

