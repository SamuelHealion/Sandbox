"""
CP1404 Week 9 Lecture notes - Do this now
Define the class Student
"""

from person import Person


class Student(Person):
    """Represents a Student object."""

    def __init__(self, first_name, last_name, age, student_id=0):
        """Initialize a Student instance."""
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def __str__(self):
        """Return a string representation of a Student object."""
        return "{} {} is {}. Their student number is {}."\
            .format(self.first_name, self.last_name, self.age, self.student_id)


def run_tests():
    sam = Student('Samuel', 'Healion', 28, 12595998)
    print(sam)


if __name__ == '__main__':
    run_tests()
