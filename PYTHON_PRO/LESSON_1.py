import datetime


class Student:
    count = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        Student.count += 1  # чтобы посмотреть кол-во студентов (инстансов)

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age}'


class Group:
    def __init__(self, course, students=None):
        if isinstance(students, list):
            self.students = students
        else:
            self.students = []

        self.title = f'{course} - {datetime.date.today()}'

    def __str__(self):
        res = f'{self.title}:\n'
        res += '\n'.join(map(str, self.students))
        return res


st_1 = Student('Ivan', 'Ivanov', 20)
st_2 = Student('Petr', 'Ivanov', 20)

group = Group('Python')
group.students.append(st_1)
group.students.append(st_2)
print(group)
print(Student.count)
