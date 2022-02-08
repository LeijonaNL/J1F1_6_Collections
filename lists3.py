# Lists3

import random

spellen = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def function():
    eindlijst = list()
    for i in range(10):
        eindlijst.append(spellen[random.randint(0,len(spellen)-1)])
    print(eindlijst)

function()
#print(spellen)