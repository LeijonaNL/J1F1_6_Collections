# Lists

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


print('All days of the week:')
for i in range(0, 7):
    print(days[i])

print('\nAll work days:')
for i in range(0, 5):
    print(days[i])

print('\nAll weekend days:')
for i in range(5, 7):
    print(days[i])

print('\nAll days of the week, reverse:')
for i in range(7, 0, -1):
    print(days[i])

print('\nAll work days, reverse:')
for i in range(5, 0, -1):
    print(days[i])

print('\nAll weekend days, reverse:')
for i in range(7, 5, -1):
    print(days[i])