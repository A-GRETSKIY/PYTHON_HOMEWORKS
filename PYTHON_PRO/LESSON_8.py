x = range

print(list(x(10, 20)))


            ###


def func(x, a, b):
    print(*x(a, b))


func(range, 10, 20)


            ###


def func():
    return sum


res = func()

print(res(range(10, 20)))


            ###


import random

seq = [random.randint(1, 100) for i in range(50)]


def filter_seq(seq, predicate):
    return [item for item in seq if predicate(item)]


def rule_1(item):
    return item % 2


def rule_2(item):
    return not item % 2


print(filter_seq(seq, rule_1))
print(filter_seq(seq, rule_2))
print(filter_seq(seq, lambda item: 1 < item < 10))


            ###


def calculate_pow(n):
    def calculate(number):
        return number ** n
    return calculate


x = calculate_pow(3)
print(x(2))
print(x(4))
print(x(6))


            ###


def calculate_pow(n):
    x = 2
    def calculate(number):
        return number ** n
    return calculate


f = calculate_pow(3)
print(f.__code__.co_freevars)
print(f.__closure__)


            ###


my_function = []


def register_func(f):
    my_function.append(f)
    return f


@register_func
def sum(x, y):
    return x + y


@register_func
def mul(x, y):
    return x * y


print(my_function)

print(sum(10, 20))
print(mul(10, 20))


            ###


def get_text():
    return 'Hello, world'


def bold_wrapper(func):
    def inner():
        return f'<b>{func()}</b>'
    return inner


def italic_wrapper(func):
    def inner():
        return f'<i>{func()}</i>'
    return inner


def paragraph_wrapper(func):
    def inner():
        return f'<p>{func()}</p>'
    return inner


print(italic_wrapper(bold_wrapper(get_text))())


            ##########


def bold_wrapper(func):
    def inner():
        return f'<b>{func()}</b>'
    return inner


def italic_wrapper(func):
    def inner():
        return f'<i>{func()}</i>'
    return inner


def paragraph_wrapper(func):
    def inner():
        return f'<p>{func()}</p>'
    return inner


@bold_wrapper
@paragraph_wrapper
@italic_wrapper
def get_text():
    return 'Hello, world'


print(get_text())