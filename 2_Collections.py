import random
"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
"""
# List of all lowercase letters to use as keys in the dictionaries
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

def create_list(l = letters):
    a = []  # Initialize an empty list to store the dictionaries
    # Loop to generate between 2 and 10 dictionaries
    for i in range(2, 10):
        usedKeys = []  # List to keep track of used keys for the current dictionary
        dictForAdding = {}  # Initialize an empty dictionary for the current iteration
        while len(dictForAdding) < 3:  # Ensure each dictionary has exactly 3 key-value pairs
            usedKey = random.choice(l)  # Randomly select a letter as the key
            usedKeys.append(usedKey)  # Add the selected key to the list of used keys
            dictForAdding[usedKey] = random.randint(0, 100)  # Assign a random value (0-100) to the key
        a.append(dictForAdding)  # Append the generated dictionary to the list
    return a

a = create_list()
print("a: ", a)  # Print the generated list of dictionaries

"""
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

Commit script to git repository and provide link as home task result.
"""
def change_list(l  = letters):
    duplicatedDict = {} # Initialize an empty dictionary to store keys and their occurrences across dictionaries
    for letter in l:
        tempDict = {}  # Temporary dictionary to store occurrences of the current key
        for dictA in a:  # Loop through each dictionary in the list
            if letter in dictA.keys():  # Check if the current key exists in the dictionary
                dictACopy = dictA.copy()  # Create a copy of the dictionary to avoid modifying the original
                tempDict[a.index(dictA)] = dictACopy.pop(letter)  # Store the value of the key and its dictionary index
                """
                if letter in duplicatedDict.keys():  # If the key already exists in `duplicatedDict`
                    duplicatedDict[letter] = duplicatedDict.get(letter) | tempDict  # Merge occurrences
                else:
                    duplicatedDict[letter] = tempDict  # Add the key and its occurrences to `duplicatedDict`"""
                duplicatedDict[letter] = duplicatedDict.get(letter) | tempDict if letter in duplicatedDict.keys() else tempDict
    #print("\nduplicatedDict: ", duplicatedDict)

    # Process the `duplicatedDict` to create the final combined dictionary
    for key, values in duplicatedDict.items():
        if len(values) != 1:  # If the key exists in more than one dictionary
            # print("\nvalues: ", values)
            mk = -1  # Initialize the index of the dictionary with the max value
            mv = 0  # Initialize the max value
            for i in range(len(values) - 1):  # Loop through the occurrences of the key
                try:
                    del values[mk]  # Delete the previous max value entry (if any)
                    mv = 0  # Reset the max value
                    mk = -1  # Reset the index of the dictionary with the max value
                except:
                    pass
                for k, v in values.items():  # Loop through the key-value pairs in `values`
                    if v > mv:  # Check if the current value is greater than the max value
                        mv = v  # Update the max value
                        mk = k  # Update the index of the dictionary with the max value
                # print("\tmk: ", mk)
                # print("\tmv: ", mv)
                # print("\tkey: ", key)
                newKey = key + '_' + str(len(values) - 1)  # Rename the key with the dictionary number
                # print("\tnewKey ", newKey)
                # print("\t ", a[mk])
                a[mk][newKey] = a[mk].pop(key)  # Update the dictionary with the renamed key and max value

change_list(letters)
print("a: ", a)  # Print the final list of dictionaries




