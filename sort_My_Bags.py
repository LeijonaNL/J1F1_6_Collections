# Sort my bags!

import random, os, time
os.system("cls")

colorsL = ['orange', 'blue', 'green', 'brown']
colorsD = {
    "orange": 0,
    "blue": 0,
    "green": 0,
    "brown": 0
}

def bagMnM(collectionType, amount):
    if isinstance(collectionType, list):
        bagL = list()
        for i in range(amount):
            bagL.append(random.choice(colorsL))
        return bagL
    elif isinstance(collectionType, dict):
        for i in range(amount):
            colorsD[random.choice(colorsL)] += 1
        return colorsD

def sortMM(unsorted):
    if isinstance(unsorted, list):
        unsorted = list()
        unsorted.sort()
        return unsorted
    elif isinstance(unsorted, dict):
        sortedBag = dict(sorted(bagUnsorted.items(), key=lambda item: item[1], reverse = True))
        return sortedBag 

bagChoice = input("\nWhat sort of bag would you like to fill?\n1. list bag\n2. dictionairy bag\n").upper().replace(" ", "")\
    .replace("BAG", "").replace("IST", "").replace("ICTIONAIRY", "")
if bagChoice == "L" or bagChoice == "1":
    collectionChoice = colorsL
elif bagChoice == "D" or bagChoice == "2":
    collectionChoice = colorsD
time.sleep(0.5)
MnMamount = int(input("\nHow many MnMs would you like in the bag?\n"))
time.sleep(0.5)
bagUnsorted = bagMnM(collectionChoice, MnMamount)
bag = sortMM(bagUnsorted)
print(bag)