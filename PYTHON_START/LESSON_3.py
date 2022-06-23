money = float(input('Your money: '))
apples = 20
if money >= apples:
    print(f'You can buy {money // apples} kg of apples')
else:
    print('Bad day')
print('Good luck!')

day = int(input('Day= '))
if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
else:
    print('Error')

# ЗАДАЧА НА СОБЕСЕДОВАНИИ
n = 1
if n == 1:
    n = 0
elif n == 0:
    print('Hello')
elif n <= 0:
    print('world')
else:
    print('Error')

a = 20
b = 30
if a == 20 and b == 30:
    print('Ok')