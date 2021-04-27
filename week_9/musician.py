"""
CP1404 Week 9 Lecture notes - Do this now
Define the class Musician
"""

from person import Person


class Musician(Person):
    """Represents a Musician object."""

    def __init__(self, first_name, last_name, age, instrument=''):
        """Initialize a Musician instance."""
        super().__init__(first_name, last_name, age)
        self.instrument = instrument

    def __str__(self):
        """Return a string representation of a Musician object."""
        return "{} {} is {} years old and plays the {}." \
            .format(self.first_name, self.last_name, self.age, self.instrument)

    def play(self, duration):
        """Make the Musician play for a chosen duration."""
        print("{} {} plays the {} for {} minutes."
              .format(self.first_name, self.last_name, self.instrument, duration))


def run_tests():
    sam = Musician('Samuel', 'Healion', 28, 'Piano')
    print(sam)
    sam.play(60)


if __name__ == '__main__':
    run_tests()
