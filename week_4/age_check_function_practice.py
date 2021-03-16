"""
Function practice that asks for a users age from week_4 Live lecture
"""


def main():
    user_age = get_valid_age()
    print("You are {} years old".format(user_age))


def get_valid_age():
    valid_age = False
    while not valid_age:
        try:
            user_age = int(input("Please enter your age: "))
            if user_age < 0:
                print("Please enter a non-negative age")
            else:
                valid_age = True
        except ValueError:
            print("Please enter a number")
    return user_age


main()
