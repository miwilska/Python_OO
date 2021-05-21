from abc import abstractmethod, ABC
import math


class Shape(ABC):
    def __init__(self, a1=1, a2=2, a3=3, a4=4, a5=5, a6=6):
        self.set_params(a1, a2, a3, a4, a5, a6)

    def set_params(self, a, b, c, d, e, f):
        self._a1 = a
        self._a2 = b
        self._a3 = c
        self._a4 = d
        self._a5 = e
        self._a6 = f

    def get_a(self):
        return self._a1

    def get_b(self):
        return self._a2

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a1) + " , " + str(self._a2) \
               + " , " + str(self._a3) + " , " + str(self._a4) \
               + " , " + str(self._a5) + " , " + str(self._a6) \
               + "] at " + str(hex(id(self)))

    @abstractmethod
    def calc_surface(self):
        return 0

    @abstractmethod
    def calc_perimeter(self):
        return 0


class Shape3D(ABC):

    @abstractmethod
    def calc_volume(self):
        return 0


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b)

    def calc_surface(self):
        return self._a1 * self._a2

    def calc_perimeter(self):
        return 2 * (self._a1 + self._a2)

    def __repr__(self):
        return self.__class__.__name__ + "[a=" + str(self._a1) + "b=" + str(self._a2) + "] at " + str(hex(id(self)))


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def __repr__(self):
        return self.__class__.__name__ + "[a=" + str(self._a1) + "] at " + str(hex(id(self)))


class Cube(Square, Shape3D):

    def calc_volume(self):
        return self._a1 ** 3

    def calc_surface(self):
        return 6 * super().calc_surface()


class Circle(Shape):
    def __init__(self, r):
        super().__init__(r)

    def calc_surface(self):
        return math.pi * self._a1 ** 2

    def calc_perimeter(self):
        return 2 * (self._a1 * math.pi)

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a1) + "] at " + str(hex(id(self)))


class Sphere(Circle, Shape3D):
    def calc_volume(self):
        return 4 / 3 * math.pi * self._a1 ** 3

    def calc_surface(self):
        return 4 * super().calc_surface()


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def calc_perimeter(self):
        return self._a1 + self._a2 + self._a3

    def calc_surface(self):
        a = self._a1
        b = self._a2
        c = self._a3
        p = (1 / 2) * (a + b + c)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s

    def __repr__(self):
        return self.__class__.__name__ + "[ a=" + str(self._a1) + ", b=" + str(self._a2) + ", c=" + str(self._a3) \
               + "] at " + str(hex(id(self)))


class EquilateralTriangle(Triangle):
    def __init__(self, a, b, c):
        if c == math.sqrt(a ** 2 + b ** 2):
            super().__init__(a, b, c)
        else:
            print("it is not possible with {0}, {1} and {2} - it is not equilateral triangle".format(a, b, c))


## tests
e_trian = EquilateralTriangle(3, 4, 5)
print(e_trian)
e_trian = EquilateralTriangle(1, 3, 4)

# 2D shapes
rectangle = Rectangle(5, 6)
circle = Circle(7)
triangle = Triangle(30, 40, 50)

shape_list = [rectangle, circle, triangle]
print()
print('--------------------')
for sh in shape_list:
    print(sh.__class__.__name__)
    # sh.set_params(3, 4, 5, 6, 7, 8)
    print(sh)
    print("surface: ")
    print(sh.calc_surface())
    print("perimeter: ")
    print(sh.calc_perimeter())

sphere = Sphere(8)
cube = Cube(3)

shape_3D_list = [cube, sphere]
print()
print('--------------------')
for sh in shape_3D_list:
    print(sh.__class__.__name__)
    print(sh)
    print("surface: ")
    print(sh.calc_surface())
    print("volume: ")
    print(sh.calc_volume())
