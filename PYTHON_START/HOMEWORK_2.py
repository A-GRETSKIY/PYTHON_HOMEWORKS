            # 1. Write a Python program to print the number entered by user only if the
            # number entered is negative.

x = int(input('Введите число '))
print(x < 0 and x or 'Больше или равно нулю')

            # 2. Write a Python program to check if the value a is less than 20 or not.

x = int(input('Введите число '))
print(x < 20 and x or 'Больше или равно 20')

            # 3. Write a Python program to check if a given number is Zero or Not.

            # Exemple 1

x = int(input('Введите число '))
print(x == 0)

            # Exemple 2

x = int(input('Введите число '))
print(not bool(x))

            # Exemple 3

x = int(input('Введите число '))
print(not x)

            # 4. Write a Python program to check if a given number is Even or Odd.

            # Exemple 1

x = int(input('Введите число: '))
print((x % 2 and 'Число нечетное') or 'Число четное')

            # Exemple 2

x = int(input('Введите число: '))
print(not x % 2)
print(bool(x % 2))

            # 5. Write a Python program to find largest number among three numbers
            # entered by user.

            # Exemple 1

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
print('Максимальное число: ', max(a, b, c))

            # Exemple 2

a, b, c = map(int, input("Введите значение чисел: ").split())
print(max(a, b, c))
