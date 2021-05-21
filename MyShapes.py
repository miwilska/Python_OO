from abc import abstractmethod, ABC


class Shape(ABC):
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self._b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self._b) + "] at " + str(hex(id(self)))

    @abstractmethod
    def calc_surface(self):
        return 55

    @abstractmethod
    def calc_perimeter(self):
        return 55


class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self._b

    def calc_perimeter(self):
        return (self._a + self._b) * 2

    def swap_sides(self):
        a = self._a
        b = self._b
        self._a = b
        self._b = a


class Squere(Rectangle):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, a)
        # self._a = a


import math


class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        # self._a = a

    def calc_surface(self):
        return math.pi * self._a ** 2

    def calc_perimeter(self):
        return (self._a * math.pi) * 2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class Sphere(Circle):
    def calc_volume(self):
        return 4 / 3 * math.pi * self._a ** 3

    def calc_surface(self):
        return 4 * super().calc_surface()


class Triangle(Shape):
    def __init__(self, a=3, b=4, c=5):
        self._a = a
        self._b = b
        self._c = c
        self._h = None

    def __int__(self, a=3, h=4):
        self._a = a
        self._h = h

    def set_params(self, par_a, par_b):
        self._a = par_a
        self._b = par_b
        self._c = math.sqrt(par_a * par_a + par_b * par_b)

    def calc_perimeter(self):
        if self._h is None :
            p= self._a + self._b + self._c
        else :
            p =0
        return p
    def calc_surface(self):
        if self._h is not None:
            s = (1 / 2) * self._a * self._h
        else:
            a = self._a
            b = self._b
            c = self._c
            p = (1 / 2) * (a + b + c)
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + ", " + str(self._b) + ", " + str(self._c) + "] at " + str(
            hex(id(self)))


# class EquilateralTriangle(Triangle):
#   def

a = None
b = None
c = None

rectangle = Rectangle(5, 6)
print(rectangle)
# rectangle._a = 600
print(rectangle.calc_surface())
rectangle.swap_sides()
r_desc = str(rectangle)
print(r_desc)

circle = Circle(7)
c_desc = str(circle)
print(c_desc)
print(circle.calc_surface())

sphere = Sphere(8)
print(sphere)
print('sphere volume: ')
print(sphere.calc_volume())
print('sphere surface:')
print(sphere.calc_surface())

triangle = Triangle(30, 40, 50)
t_desc = str(triangle)
print(triangle)
print('triangle surface:')
print(triangle.calc_surface())

shape_list = [rectangle, circle, sphere, triangle]
print()
print('--------------------')
for sh in shape_list:
    print(sh.__class__.__name__)
    sh.set_params(10, 15)
    print(sh.calc_surface())
    print(sh.calc_perimeter())
