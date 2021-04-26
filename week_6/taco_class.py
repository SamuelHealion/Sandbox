"""
CP1404 Week 6 Lectures
Practicing using classes
"""


class User(object):

    def __init__(self, name=''):
        self.name = name
        self.number_of_tacos = 5
        self.score = 0

    def give_taco(self, other):
        self.number_of_tacos -= 1
        self.score += 2
        other.number_of_tacos += 1

    def __repr__(self):
        return "{}, {} points, {} tacos left".format(self.name, self.score, self.number_of_tacos)


u1 = User('Sam')
u2 = User('Ellie')

u1.give_taco(u2)
u2.give_taco(u1)

print(u1)
print(u2)
