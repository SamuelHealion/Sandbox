"""
Takes in a list of scores until a negative number is entered and then prints the highest score
From CP1404 week_4 Equality Lecture
"""

scores = []
try:
    score = int(input("Score: "))
    while score >= 0:
        scores.append(score)
        score = int(input("Score: "))
    print("Your highest score is ", max(scores))
except ValueError:
    print("That was an invalid input")
