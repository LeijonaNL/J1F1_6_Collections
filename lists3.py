# Lists3

import random, os
os.system("cls")

gameList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def gameProgram(gameList, minimum: 3, maximum: 11):
    lijst = list()
    for i in range(random.randint(minimum, maximum)):
        lijst.append(random.choice(gameList))
    return lijst

minimum = int(input("What would you like to be the minimum amount of games displayed in the list?\n"))
maximum = int(input("\nAnd the maximum?\n"))
if minimum > maximum:
    maximum = minimum
    minimum = maximum

games = gameProgram(gameList, minimum, maximum)
print(games)