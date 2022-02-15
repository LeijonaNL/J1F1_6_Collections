# Nutty

import random, os
os.system("cls")

colorsL = ['orange', 'blue', 'green', 'brown']

def zakMnMF(amount):
    colorsD = {
    "orange": 0,
    "blue": 0,
    "green": 0,
    "brown": 0
}
    for i in range(amount):
        colorsD[random.choice(colorsL)] += 1
    return colorsD

amount = int(input("How many MnMs? "))
zakMnM = zakMnMF(amount)
print(zakMnM)