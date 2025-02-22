class Rectangle:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self.__a = a
        self.b = par_b

    def calc_surface(self):
        return self.__a*self.b

    def get_a(self):
        return self.__a

    def __repr__(self):
        return "Rectangle[" + str(self.__a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle(5, 6)
r.a = 10
r.__a = 8
print(r)
print('__a in rectangle is: ' + str(r.get_a()))
print('rectangle.__a in is: ' + str(r.__a))
print('rectangle.a in is: ' + str(r.a))
