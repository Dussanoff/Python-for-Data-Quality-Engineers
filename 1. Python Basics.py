import random

#create list of 100 random numbers from 0 to 1000
a = []  # Initialize an empty list to store the random numbers
for i in range(100):  # Loop 100 times to generate 100 random numbers
    a.append(random.randint(0, 1000))  # Generate a random integer between 0 and 1000 and append it to the list
    #print(a[i])
#print('\n\n')


#sort list from min to max (without using sort())
for i in range(len(a)):  # Outer loop to iterate through the list
    aSorted = True  # Initialize a flag to check if the list is already sorted
    for j in range(len(a)-i-1):  # Inner loop to compare adjacent elements
        if a[j] > a[j+1]:  # If the current element is greater than the next element
            a[j], a[j+1] = a[j+1], a[j]  # Swap the two elements
            aSorted = False  # Set the flag to False since a swap occurred
    if aSorted:  # If no swaps occurred in the inner loop, the list is already sorted
        break  # Exit the outer loop early to save computation
"""
for i in range(len(a)):
    print(a[i])
"""


#calculate average for even and odd numbers
evenSum = 0  # Initialize the sum of even numbers to 0
oddSum = 0  # Initialize the sum of odd numbers to 0
evenCount = 0  # Initialize the count of even numbers to 0
oddCount = 0  # Initialize the count of odd numbers to 0
for i in range(len(a)):  # Loop through the sorted list
    if a[i] % 2 == 0:  # Check if the current number is even
        evenSum = evenSum + a[i]  # Add the even number to the even sum
        evenCount += 1  # Increment the even number count
    else:  # If the current number is odd
        oddSum = oddSum + a[i]  # Add the odd number to the odd sum
        oddCount += 1  # Increment the odd number count

evenAvg = evenSum / evenCount  # Average of even numbers = total sum of even numbers / count of even numbers
oddAvg = oddSum / oddCount  # Average of odd numbers = total sum of odd numbers / count of odd numbers

#print both average result in console
print(evenAvg, '\n', oddAvg)  # Print the average of even numbers and the average of odd numbers on separate lines
