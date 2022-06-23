class Person:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender


    def __str__(self):
        return f'{self.surname} {self.name}, {self.gender}'


class Student(Person):
    count = 0

    def __init__(self, age: int, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.age = age

        Student.count += 1

    def __str__(self):
        return f'{self.surname} {self.name}, {self.gender}, {self.age}'

# Создайте класс Группа, который содержит список  из 10
# объектов класса Студент. Реализуйте методы добавления,
# удаления студента и метод поиска студента по фамилии.
# Определите для Группы метод __str__() для возвращения списка
# студентов в виде строки


class Group:
    def __init__(self, course, students=None):
        if isinstance(students, list):
            self.students = students
        else:
            self.students = []

        self.title = f'{course}'

    def __str__(self):
        res = f'{self.title}:\n'
        res += '\n'.join(map(str, self.students))
        return res


st_1 = Student('Ivan', 'Ivanov', 'M', 20)
st_2 = Student('Ivan', 'Ivanov', 'M', 20)
st_3 = Student('Ivan', 'Ivanov', 'M', 20)
st_4 = Student('Ivan', 'Ivanov', 'M', 20)
st_5 = Student('Ivan', 'Ivanov', 'M', 20)
st_6 = Student('Ivan', 'Ivanov', 'M', 20)
st_7 = Student('Ivan', 'Ivanov', 'M', 20)
st_8 = Student('Ivan', 'Ivanov', 'M', 20)
st_9 = Student('Ivan', 'Ivanov', 'M', 20)
st_10 = Student('Ivan', 'Ivanov', 'M', 20)