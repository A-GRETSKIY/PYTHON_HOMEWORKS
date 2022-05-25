# Homework 3
# 1. Write a Python program to print the number entered by user only if the number entered is negative.
# 2. Write a Python program to check if the value a is less than 20 or not.
# 3. Write a Python program to check if a given number is Zero or Not.
# 4. Write a Python program to check if a given number is Even or Odd.
# 5. Write a Python program to find largest number among three numbers entered by user.

x = int(input('Введите число '))
print(x < 0 and x or 'Больше или равно нулю')

###

x = int(input('Введите число '))
print(x < 20 and x or 'Больше или равно 20')

###

x = int(input('Введите число '))
print(x == 0)

###

# x = int(input('Введите число '))
# print(not bool(x))
#
# x = int(input('Введите число '))
# print(not x)

###

x = int(input('Введите число: '))
print((x % 2 and 'Число нечетное') or 'Число четное')

###

# x = int(input('Введите число: '))
# print(not x % 2)
# print(bool(x % 2))

###

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
print('Максимальное число: ', max(a, b, c))

###

a, b, c = map(int, input("Введите значение чисел: ").split())
print(max(a, b, c))
