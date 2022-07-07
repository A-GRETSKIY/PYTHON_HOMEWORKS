try:
    x, y = int(input('x = ')), int(input('y = '))
    print(f'x // y = {x // y}')
except:
    print('Error')

                    ###

x, y = int(input('x = ')), int(input('y = '))
try:
    print(f'x // y = {x // y}')
except ZeroDivisionError:
    print('ZeroDivisionError')

                    ###

x, y = int(input('x = ')), int(input('y = '))
try:
    print(f'x // y = {x // y}')
except ZeroDivisionError as error:
    print('ZeroDivisionError', error)

                    ###

try:
    x, y = int(input('x = ')), int(input('y = '))
    print(f'x // y = {x // y}')
except ValueError as error:
    print('Я жду только целое число\n', error)
except ZeroDivisionError as error:
    print('На ноль делить нельзя\n', error)

                    ### зацикливание while True: + break

while True:
    try:
        x, y = int(input('x = ')), int(input('y = '))
        print(f'x // y = {x // y}')
        break
    except ValueError as error:
        print('Я жду только целое число\n', error)
    except ZeroDivisionError as error:
        print('На ноль делить нельзя\n', error)

                    ###

def summa(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Args must be int')
    return a + b