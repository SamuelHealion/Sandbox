"""
Counts the number of vowels in a user's name. From week_4 Lecture recordings for CP1404
"""

VOWELS = "AEIOU"


def main():
    # name = input("Name: ")
    name = "Bobby McAardvark"
    # print("Out of {} letters, {} has {} vowels".format(alpha_counter(name), name, vowel_counter(name)))
    capitals = [c for c in name if c.isupper()]
    vowels = [c for c in name if c.upper() in VOWELS]
    new_name = "".join([c for c in name if c.upper() not in VOWELS])
    # print(capitals)
    # print(vowels)
    print(new_name)


def vowel_counter(name):
    """Returns the number of vowels in a string"""
    number_of_vowels = 0
    for char in name:
        if char.upper() in VOWELS:
            number_of_vowels += 1
    return number_of_vowels


def alpha_counter(name):
    """Returns the number of alphabetical letters in a string"""
    number_of_letters = 0
    for char in name:
        if char.isalpha():
            number_of_letters += 1
    return number_of_letters


main()
