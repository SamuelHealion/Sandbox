"""
CP1404 Week 9 Lecture notes - Do this now
Define the class Person
"""


class Person:
    """Represents a Person object."""

    def __init__(self, first_name='', last_name='', age=0):
        """Initialise the Person instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Return a string representation of a Person object."""
        return "{} {}, {} years old".format(self.first_name, self.last_name, self.age)

    def __lt__(self, other):
        """Less than, used to sort people by age, from youngest to oldest."""
        return self.age < other.age

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name and self.age == other.age:
            return True


def run_tests():
    first_person = Person('Sam', 'Healion', 28)
    print(first_person)
    second_person = Person('Sam', 'Healion', 28)
    print(second_person)
    if first_person == second_person:
        print('They are the same person')


if __name__ == '__main__':
    run_tests()
