# Nutty
colorsL = ['orange', 'blue', 'green', 'brown']
import random, os
os.system("cls")

colorsD = {
    "orange": 0,
    "blue": 0,
    "green": 0,
    "brown": 0
}

amount = int(input("How many MnMs? "))
def zakMnMF(amount):
    for i in range(amount):
        colorsD[colorsL[random.randint(0,len(colorsL)-1)]] += 1
    return colorsD
zakMnM = zakMnMF(amount)
print(zakMnM)