
                                        ### LESSON 9 ###

            ### ФУНКЦИЯ, ЧИСЛО ЧЕТНОЕ ИЛИ НЕЧЕТНОЕ ???
            # V.1

def is_odd(x):
    if x % 2:
        return 'Odd'
    else:
        return 'Even'
print(is_odd(2))
print(is_odd(3))

            # V.2

def is_odd(x):
    if x % 2:
        return 'Odd'
    return 'Even'
print(is_odd(2))
print(is_odd(3))

            # V.3

def is_odd(x):
    return 'Odd' if x % 2 else 'Even'
print(is_odd(2))
print(is_odd(3))


            ### ### ###

def outer(x, y):
    c = 200
    def summa(a, b):
        return a + b + c
    return summa(x, y)
print(outer(10, 20))

            ### ### ###

def summa(a, b, c=20):
    return a + b + с
print(summa(10, 20))  ### результат = 50
print(summa(10, 20, 200))  ### результат = 230

            ### ### ###

def summa(a, b, c=20):
    return a + b + с
print(summa(b=20, a=10)) ### результат = 50
print(summa(b=100, a=20, c=100)) ### результат = 130

            ### ### ###

x = 20


def func(a, b):
    global x  ### ЧЕРЕЗ "ГЛОБАЛ" ГОВОРЮ, ЧТО ВНУТРИ ФУНКЦИИ БУДУ РАБОТАТЬ С ГЛОБАЛЬНОЙ ОБЛАСТЬЮ
    x = 90
    return a + b + x


print(func(10, 20))
print(x)


            ### ### ###

            # 1. СКОЛЬКО СЛОВ
            # 2. СКОЛЬКО СИМВОЛОВ
            # 3. СКОЛЬКО ПРЕДЛОЖЕНИЙ

def words(x):
    return len(x.split())
x = input('Text: ')
print(words(x))

def simbol(a):
    return(len(a))
a = input('Text: ')
print(simbol(a))

def sentence(b):
    return len(b.split('.'))
b = input('Text: ')
print(sentence(b))

            ### ### ###

            # 1. СКОЛЬКО СЛОВ
            # 2. СКОЛЬКО СИМВОЛОВ
            # 3. СКОЛЬКО ПРЕДЛОЖЕНИЙ

def words(x):
    return len(x.split())


def simbol(x):
    return (len(x))


def sentence(x):
    return len(x.split('.'))


x = input('Text: ')

print(words(x))
print(simbol(x))
print(sentence(x))

            ### ### ###

def summa(a: int | float, b: int | float):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)): # isinstance - проверяет, принадлежит ли объект определенному типу
        return a + b
    return None
print(summa(2, 3))
print(summa('4', '7'))

            ### ### ###

def filter_odd(seq):
    res = [item for item in seq if item % 2]
    return res

def filter_even(seq):
    res = [item for item in seq if not item % 2]
    return res

x = [1, 2, 3, 4, 5, 6, 7]
print(filter_odd(x))
print(filter_even(x))

                  ### ### - ЛУЧШИЙ ВАРИАНТ С ФУНКЦИЕЙ LAMBDA

def filter(seq, func):
    res = [item for item in seq if func(item)]
    return res

x = [1, 2, 3, 4, 5, 6, 7]
print(filter(x, lambda item: item % 2))  # возвр.нечет.
print(filter(x, lambda item: not item % 2))  # возвр.чет.
print(filter(x, lambda item: item))  # возвр.все
print(filter(x, lambda item: item > 5))  # возвр.элем.больше 5

                    ### ### ### - КАЛЬКУЛЯТОР С ПОМОЩЬЮ СЛОВАРЯ И ФУНКЦИИ LAMBDA

res = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

a, b = int(input('a=')), int(input('b='))
op = input('operation is ')

x = res[op]
print(x(a, b))

                    ### ### ###

x = [1, 2, 3, 4]
def func(y):
    y.append(100)
func(x)   ### func(x[:]) - СОЗДАЕМ КОПИЮ, ЧТОБЫ НЕ МЕНЯТЬ ГЛОБАЛЬНЫЙ ОБЪЕКТ
print(x)

                    ### ### ###

# # СМС-РАССЫЛКА
#
# gender = {
#     'm': 'Дорогой',
#     'f': 'Дорогая'
# }
#
# a = [
#     ['Семен', 'Семенович', 32.56, 'm'],
#     ['Тамара', 'Ивановна', 12.67, 'f'],
#     ['Михаил', 'Сергеевич', 32.56, 'm'],
# ]
#
# for name, surname, balance, g in a:
#     text = f'''{gender[g]} {name} {surname}, баланс вашего лицевого счета
# составляет {balance} гривен'''
#     print(text)

text = input()
text = set(text.split())
print(text)  ### ВЫВОД СЛОВ БЕЗ ДУБЛИКАТОВ

text = input()
vowels = {'а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е'}  # УКАЗАНЫ В НИЖНЕМ РЕГИСТРЕ, ВЫБЕРЕТ ТОЛЬКО ИХ
res = set(text) & vowels
print(res)  ### ПОСЧИТАТЬ КОЛИЧЕСТВО ГЛАСНЫХ В ТЕКСТЕ

cats = [
    {
        'name': 'Tom',
        'color': 'black',
        'age': 2,
        'breed': 'Sphynx',
        'address': {
            'city': 'Chernihiv',
            'street': 'Lyotna',
            'home': 43
        }
    },
    {
        'name': 'Tom',
        'color': 'black',
        'age': 5,
        'breed': 'Scotish',
        'address': {
            'city': 'Kyiv',
            'street': 'Uspenska',
            'home': 12
        }
    }
]
print(cats)
for item in cats:
    print(item['name'])


                    ### ### ###

            # ФАКТОРИАЛ ЧЕРЕЗ РЕКУРСИЮ

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


print(fact(5))

            # СТЕПЕНЬ ЧИСЛА ЧЕРЕЗ РЕКУРСИЮ

def my_pow(a, b):
    if b == 0:
        return 1
    return a * my_pow(a, b - 1)


print(my_pow(2, 3))

            # РЕКУРСИЯ

def print_i(n):
    if n == 0:
        return
    print(n)
    print_i(n-1)


print_i(10)  ### выведет числа от 10 до 1

        # НАОБОРОТ ОТ 1 ДО 10:

def print_i(n):
    if n == 0:
        return

    print_i(n-1)
    print(n)

print_i(10)   ### выведет числа от 1 до 10

