# Homework 2
# 1. Construct an integer from the string "123"
# 2. Construct a float from the integer 123
# 3. Construct an integer from the float 12.345
# 4. Write a Python-script that detects the last 4 digits of a credit card
# 5. Write a Python-script that calculates the sum of the digits of a three-digit number
# 6. Write a program that calculates and displays the area of a triangle if its sides are known
# 7. *Write a Python-script that calculates the sum of the digits of a number
# 8. *Determine the number of digits in a number
# 9. *Print the digits in reverse order

a = int(str('123'))
print(a)

###

a = float(int(123))
print(a)

###

a = int(float(123.45))
print(a)

###

d = int(input('Введите номер карты: '))
print('Последние 4 цифры: ', d % 10000)

###

x = int(input('Введите 3-х значное число: '))
print(x // 100 + x // 10 % 10 + x % 10)

###

print('Введите длинну сторон треугольника')
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('Площадь треугольника =', s)

###

a = input('Введите число: ')
a = sum(map(int, str(a)))
print('Сумма цифр: ', a)

###

a = input('Введите число: ')
print('Колличество цифр: ', len(a))

###

a = input('Введите число: ')
print('Цифры в обратном порядке: ', a[::-1])
