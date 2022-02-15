# Deez nuts

import random, os
os.system("cls")

colors = ['orange', 'blue', 'green', 'brown']

amount = int(input("How many M&Ms? "))

def zak(amount):
    zakMM = list()
    for i in range(amount):
        zakMM.append(random.choice(colors))
    return zakMM

bag = zak(amount)
print(bag)