            # 1.Напишите программу, которая считает две строки текста с клавиатуры и
            # выведет на экран буквы, которые есть одновременно и в первой, и во
            # второй строке. Например, для строк «Hello» и «World» на экране должны
            # быть буквы «l» и «o».

text_1 = set(input('text_1 = '))
text_2 = set(input('text_2 = '))
res = text_1 & text_2
print(res)

            # 2.Напишите программу, которая сгенерирует два списка. Один с числами
            # кратными 3, другой с числами кратными 5. С помощью множеств
            # создайте список с числами, которые есть в обоих множествах.

            # Exemple 1

a = []
for i in range(3, 100, 3):
    a.append(i)
b = []
for j in range(5, 100, 5):
    b.append(j)
res = set(a) & set(b)
print(res)

            # Exemple 2

a = []
for i in range(3, 100, 3): a.append(i)
b = []
for j in range(5, 100, 5): b.append(j)
res = set(a) & set(b)
print(res) ### ЧЕРЕЗ LIST COMPREHENSIONS
