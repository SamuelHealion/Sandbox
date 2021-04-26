from shape import Shape
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle


shape = Shape(0, 0)
shape.move(10, 10)
print(shape)


rectangle = Rectangle(0, 0, 3, 2)

rectangle.move(5, 15)
print(rectangle)
print(rectangle.area())


circle = Circle(0, 0, 5)

circle.move(8, 10)
print(circle)
print(circle.area())


triangle = Triangle(0, 0, 10, 20)

triangle.move(3, 6)
print(triangle)
print(triangle.area())
