"""
Do this now for week 5 lecture
"""


def main():
    numbers = [1, 45, 634, -95, 0, -24]
    display_in_groups(numbers)


def display_in_groups(numbers):
    negative_numbers = [number for number in numbers if number < 0]
    print(negative_numbers)
    positive_numbers = [number for number in numbers if number > 0]
    print(positive_numbers)


main()
