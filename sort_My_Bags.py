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

def bagMnM():
    bagChoise = input("\nWhat sort of bag would you like to fill?\n1. list bag\n2. dictionairy bag\n").upper().replace("", "")\
    .replace("BAG", "").replace("IST", "").replace("ICTIONAIRY", "")
    time.sleep(0.5)
    amount = int(input("\nHow many MnMs would you like in the bag?\n"))
    time.sleep(0.5)
    if bagChoise == "LIST" or bagChoise == "1":
        bagL = list()
        for i in range(amount):
            bagL.append(random.choice(colorsL))
        return bagL
    elif bagChoise == "DICTIONAIRY" or bagChoise == "2":
        for i in range(amount):
            colorsD[colorsL[random.randint(0,len(colorsL)-1)]] += 1
        return colorsD

bag = bagMnM()
print(bag)