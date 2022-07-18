def n_square(n):
    i = 0
    while i < n:
        yield i ** 2
        i += 1
    return None  # можно без None и даже без return - результат один


for item in n_square(5):
    print(item)


    ###


def fibonachi(n):

    first_number = 0
    second_number = 1
    index = 1
    while index <= n:
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
        index += 1
        yield next_number
    return


for item in fibonachi(10):
    print(item)


    ###


def square_gen(n):
    i = 0
    exponent = 2
    while i <= n:
        temp_exponent = yield i**exponent
        if temp_exponent:
            exponent = temp_exponent
        i += 1

x = square_gen(5)
res = next(x)
print(res)
res = next(x)
print(res)
res = next(x)
print(res)
print(x.send(3))
res = next(x)
print(res)
res = next(x)
print(res)


    ###


x = [i for i in range(100)]
y = (i for i in range(100))
print(x)
print(y)
print(type(y))
print(list(y))


    ###


f = open('test.txt', 'w')  # открываем текстовый файл на запись
for i in range(1000):      # на 1000 строк
    f.write(f'{i}\n')      # в файл пишем строку со значением и переводом каретки
f.flush()                  #
f.close()                  # появиться файл с 1000 чисел
            #
f = open('test.txt', 'r')                # открываем тот же файл нп чтение
res = (int(line.strip()) for line in f)  # ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ (В КРУГЛЫХ СКОБКАХ)
print(sum(res))                          # посчитает сумму всех чисел