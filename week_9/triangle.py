from shape import Shape


class Triangle(Shape):
    def __init__(self, x=0, y=0, base=1, height=1):
        self.x = x
        self.y = y
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2