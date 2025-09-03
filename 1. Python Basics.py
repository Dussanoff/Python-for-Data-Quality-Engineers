import random

#create list of 100 random numbers from 0 to 1000
a = []
for i in range(100):
    a.append(random.randint(0, 1000))
    #print(a[i])
#print('\n\n')


#sort list from min to max (without using sort())
for i in range(len(a)):
    aSorted = True
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            aSorted = False
    if aSorted:
        break
"""
for i in range(len(a)):
    print(a[i])
"""


#calculate average for even and odd numbers
evenSum = 0
oddSum = 0
evenCount = 0
oddCount = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        evenSum = evenSum + a[i]
        evenCount += 1
    else:
        oddSum = oddSum + a[i]
        oddCount += 1

evenAvg = evenSum / evenCount
oddAvg = oddSum / oddCount

#print both average result in console
print(evenAvg, '\n', oddAvg)
