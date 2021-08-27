## A test to see if random.randint is skewed.

import random

## -----------------These two functions are obsolete -------------##
#Creates a list that stores the range of numbers to be tested
def createList(length):
    intList = []
    for i in range(int(length)):
        intList.append(i)
        intList.append(0)
    return intList

#Converts the list to a dictionary
def convert(list):
    resDict = {list[i]: list[i+1] for i in range(0, len(list), 2)}
    return resDict

## --------------------------------------------------------------##

#Creates a list of random numbers of the size and in the range specified by the user.
def genRandom(rangeMax, sampleSize):

    randomList = []

    for i in range(int(sampleSize)):

        randomInt = random.randint(0, rangeMax)
        randomList.append(randomInt)

    randomList.sort()

    return randomList

#Creates a dictionary with each tested int as key and its total number of occurences in the list as value.
def countResults (list):
    testDict = {}
    
    for i in range(len(list)):

        testDict.setdefault(list[i], 0)
        testDict[list[i]] = testDict[list[i]] +1

    return testDict

#Displays the total amount of occurences for each int.
def displayResults (dict):
    for k,v in dict.items():
        print(k, ": ", v)
        print("#" * v)

#Avereges the values.
def averageValue (list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    average = total / len(list)
    return average


rangeInput = input("Test range (will include all numbers from 0 up to entered number): ")
sizeInput = input("Sample size: ")

print("\n\n\n\n")
print("=" * 75)
print("\n\n")
print(" " * 10, "Range: 0-", rangeInput, " " * 10, "Sample size: ", sizeInput)
print("\n\n")
print("=" * 75)
print("\n\n\n\n")

randomList = genRandom(int(rangeInput), int(sizeInput))
displayResults(countResults(randomList))
print("\n\n")
print("Average value (the closer to median value the better):", averageValue(randomList))
print("\n\n\n\n")
