
            # 1. Есть девятиэтажный дом, в котором 4 подъезда. Номер подъезда начинается с единицы. На одном этаже 4 квартиры. Напишите
            # программу которая, получит номер квартиры с клавиатуры, и выведет на экран, на каком этаже, какого подъезда расположена эта
            # квартира. Если такой квартиры нет в этом доме, то нужно сообщить
            # об этом пользователю.
            
            # Example 1

apartment = int(input('Номер квартиры= '))
if 1 <= apartment <= 36:
    print('Подъезд 1')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 37 <= apartment <= 72:
    print('Подъезд 2')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 73 <= apartment <= 109:
    print('Подъезд 3')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif 110 <= apartment <= 144:
    print('Подъезд 4')
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
else:
    print('Данной квартиры в доме нету!')

            # Example 2

apartment = int(input('Номер квартиры = '))
if apartment <=144:
    print('Подъезд: ', (apartment - 1) // 36 + 1)
    print('Этаж: ', (apartment - 1) % 36 // 4 + 1)
elif apartment > 144:
    print('Квартиры нет в данном доме')

            # Example 3

FLOORS = 9
FLATS_IN_FLOOR = 4
for flat in range(1, 144):
    flat -= 1
    entrance = flat // (FLOORS * FLATS_IN_FLOOR) + 1
    floor = (flat - (entrance - 1) * FLOORS * FLATS_IN_FLOOR) // FLATS_IN_FLOOR + 1
    number_flat_in_floor = flat % FLATS_IN_FLOOR + 1
    print(flat + 1, entrance, floor, number_flat_in_floor, sep='\t')
    
            # 2. Определить количество дней в году, который вводит пользователь. В високосном году - 366 дней, тогда как в обычном их 365.
            # Високосный год определяется по следующему правилу: Год високосный, если он делится на четыре без остатка, но если он
            # делится на 100 без остатка, это не високосный год. Однако, если он делится без остатка на 400, это високосный год.

            # Example 1
            
x = int(input('Year: '))
if (not x % 4) and (x % 100) or (not x % 400):
    print('Год высокостный')
else:
    print('Год не высокостный')
    
            # Example 2

year = int(input('Year: '))
days = 366 if not year % 4 and year % 100 or not year % 400 else 365
print(days)

            # 3. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано: a, b, c – стороны предполагаемого
            # треугольника. Напишите программу, которая укажет, существует ли такой треугольник или нет.
            
            # Example 1

print('Введите длинну сторон треугольника')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треугольник существует')
else:
    print('Треугольник НЕ существует')
    
            # Example 2

print('Введите длинну сторон треугольника')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if a + b > c and a + c > b and b + c > a:
    print('Треугольник существует')
else:
    print('Треугольник НЕ существует')
