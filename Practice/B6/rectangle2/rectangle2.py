from rectangle import Rectangle, Square, Circle

#площадь прямоугольника
#создадим 2 прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

#вывод площади 2х прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

#площадь квадрата
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

#площадь круга
circle_1 = Circle(2)

print(circle_1.get_area_circle())



