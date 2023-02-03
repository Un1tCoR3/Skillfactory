import math

#площадь прямоугольника
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

#площадь квадрата
class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2
    #возведение в степень **2 (в квадрат)

#площадь круга
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area_circle(self):
        return math.pi * (self.radius**2)
    #площадь круга

# figures = [rect_1, rect_2, square_1, square_2, circle_1]
#     for fifure in figures:
#         if isinstance(figure, Square):
#             print(fifure.get_area_square())
#         else:
#             print(fifure.get_area())