class Animal:

    def __init__(self, age: int, color: str):
        self.age = age
        self.color = color

    def __str__(self):
        return f'{self.age}, {self.color}'


class Cat(Animal):
    def __init__(self, name: str, breed: str, age: int, color: str):
        super().__init__(age, color)  # функция super делигирует вызов метода, который находится выше по цепочке
        self.name = name
        self.breed = breed

    def __str__(self):
        return f'{self.name}, {self.breed}, {super().__str__()}'


x = Cat('Tom', 'scotish', 3, 'gray')
print(x)


                    ###


class A:

    def f_1(self):
        return 'Hello'

    def f_2(self):
        return 100


class B(A):

    def f_1(self):
        return 'Oleh'


x = B()
print(x.f_1())
print(x.f_2())


                    ## переопределение метода

class A:

    def f_1(self):
        return 'Hello'

    def f_2(self):
        return 100


class B(A):

    def f_1(self):
        return 'Oleh'


x = B()
print(x.f_1())
print(x.f_2())


                    ## переопределение метода (модификация результата)


class A:

    def f_1(self):
        return 'Hello'

    def f_2(self):
        return 100


class B(A):

    def f_1(self):
        res = super().f_1()
        return res + ', Oleh'


x = B()
print(x.f_1())
print(x.f_2())


                    ###

class A:

    def greetings(self):
        return 'Hello, from A'


class B:

    def greetings(self):
        return 'Hello, from B'


class C(A, B):  # приоритеты

    pass


x = C()

print(C.__mro__)  # метод возвращает правильную цепочку поиска
print(x.greetings())


                    ###

class A:

    def __init__(self, a, b):
        print(a, b)


class B(A):

    def __init__(self, c=None, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)

        self.c = c


x = B(a=1, b=2, c=3)
