import random
"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
a = []
for i in range(2, 10):
    usedKeys = []
    dictForAdding = {}
    while len(dictForAdding) < 3:
        usedKey = random.choice(letters)
        usedKeys.append(usedKey)
        dictForAdding[usedKey] = random.randint(0, 100)
    a.append(dictForAdding)
print(a)


