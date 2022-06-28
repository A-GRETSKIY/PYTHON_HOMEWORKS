class PriceError(Exception):

    def __init__(self, price: int | float, message):
        self.price = price
        self.message = message

    def __str__(self):
        return f'Invalid {self.price}\n {self.message}'


class Product:

    def __init__(self, title, price: int | float):
        self.title = title
        self.price = price
        if not isinstance(price, int) or not isinstance(price, float) and price <= 0:
            raise PriceError(price, 'Invalid price')

    def __str__(self):
        return f'{self.title} - {self.price}'


pr_1 = Product('apple', 343324345)

print(pr_1)


                    ###


class Person:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name.strip().title()
        self.surname = surname.strip().title()
        self.gender = gender

    def __str__(self):
        return f'{self.surname} {self.name[0]}., {self.gender}'


class Student(Person):

    def __init__(self, name: str, surname: str, gender: str, age: int):
        super().__init__(name, surname, gender)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class NumberOfStudents(Exception):
    def __init__(self, student, message):
        self.student = student
        self.message = message

    def __str__(self):
        return f'Invalid {self.student}\n {self.message}'


LIMIT = 10


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if len(self.students) >= LIMIT:
            raise NumberOfStudents(student, 'Quantity of students more then 10')
        if student not in self.students:
            self.students.append(student)

    def __str__(self):
        return '\n'.join(map(str, self.students))


students = [Student('Ivan', f'Ivanov{i}', 'M', 20 + i) for i in range(11)]
gr_1 = Group('New')
for item in students:
    gr_1.add_student(item)

print(gr_1)



