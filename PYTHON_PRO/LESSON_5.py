class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        if self.volume() > other.volume():
            return True
        return False

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'


box_1 = Box(2, 2, 2)
box_2 = Box(1, 1, 1)

print(box_1 > box_2)

            ###


class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


import random

box = [Box(random.randint(1, 15), random.randint(1, 15), random.randint(1, 15)) for i in range(10)]
print('\n'.join(map(str, box)))
print(15 * '*')
box.sort()  # box.sort(reverse = True) - в обратном порядке
print('\n'.join(map(str, box)))
