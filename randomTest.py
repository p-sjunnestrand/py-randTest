## A test to see if random.randint is skewed.

import random

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

#Creates a list of random numbers of the size and in the range specified by the user.
def genRandom(rangeMax, sampleSize):
    randomList = []
    for i in range(int(sampleSize)):
        randomInt = random.randint(0, rangeMax)
        randomList.append(randomInt)
    return randomList

testDict = {}
randomList = genRandom(10, 100)
for i in range(len(randomList)):
    print(randomList[i])
    testDict.get(randomList[i], 0)
    

#Runs the test.
# def test(randList, dict):
#     for

# print(convert(createList(10)))
# print(genRandom(10, 100))