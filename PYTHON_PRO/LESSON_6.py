class UserSeq:
    def __init__(self, number):
        self.n = number

    def __getitem__(self, item):
        if item < self.n:
            return item ** 2

        raise IndexError

    def __len__(self):
        return not self


for item in UserSeq(5):
    print(item)

                    #  что под капотом цикла for ???
i = 0
x = UserSeq(5)
while True:
    try:
        print(x[i])
        i += 1
    except IndexError:
        break

                    ###


class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'


class Group:

    def __init__(self):
        self.students = []

    def __iadd__(self, other):
        self.students.append(other)
        return self

    def __len__(self):
        return len(self.students)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start or 0  # item.start if item.start else 0
            stop = item.stop or len(self.students)
            step = item.step or 1
            if start < 0 or stop > len(self.students):
                raise IndexError()
            result = []

            for i in range(start, stop, step):
                result.append(self.students[i])
            return result

        if isinstance(item, int):
            if item < len(self.students):
                return self.students[item]
            raise IndexError()
        raise TypeError()


st_1 = Student('Ivan', 'Ivanov')
st_2 = Student('Petr', 'Petrov')
st_3 = Student('Stepan', 'Stepanov')

group = Group()
group += st_1
group += st_2
group += st_3

x = group[1:]
for item in x:
    print(item)

# for item in group:
#     print(item)

# for i, item in enumerate(group):
#     print(i, item)

                    ###


class Goods:

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}, {self.price}'


class Cart:

    def __init__(self, user):
        self.user = user
        self.goods = []

    def add(self, good):
        self.goods.append(good)

    def __str__(self):
        return '\n'.join(map(str, self.goods))

    def __iter__(self):
        return CartIter(self.goods)


class CartIter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]

        raise StopIteration


pr_1 = Goods('Apple', 1)
pr_2 = Goods('Banana', 2)
pr_3 = Goods('Orange', 3)

cart = Cart('Andrii')
cart.add(pr_1)
cart.add(pr_2)
cart.add(pr_3)

for item in cart:
    print(item)