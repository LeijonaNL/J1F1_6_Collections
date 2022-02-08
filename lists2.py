# Lists2

listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def addAndDisplayLists():
    print('-------\nAdd lists:')
    for i in range(0, 10, 1):
        x = listOne[i] + listTwo[i]
        print(f'{listOne[i]} + {listTwo[i]} = {x}')
    print('-------\n')
    
def subtractAndDisplayLists():
    print('-------\nSubtract lists:')
    for i in range(0, 10, 1):
        x =  listOne[i] - listTwo[i]
        print(f'{listOne[i]} - {listTwo[i]} = {x}')
    print('-------\n')

def multiplyAndDisplayLists():
    print('-------\nMultiply lists:')
    for i in range(0, 10, 1):
        x =  listOne[i] * listTwo[i]
        print(f'{listOne[i]} * {listTwo[i]} = {x}')
    print('-------\n')

def divideAndDisplayLists():
    print('-------\nDivide lists:')
    for i in range(0, 10, 1):
        x =  listOne[i] / listTwo[i]
        print(f'{listOne[i]} / {listTwo[i]} = {x}')
    print('-------\n')

addAndDisplayLists()
subtractAndDisplayLists()
multiplyAndDisplayLists()
divideAndDisplayLists()