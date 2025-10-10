# Write your solution here
from datetime import datetime


def how_old(day: str, month: str, year: str):
    millenium_eve = datetime(1999, 12, 31)
    dob = datetime(int(year), int(month), int(day))
    delta = millenium_eve - dob
    return delta.days

    """
    if days > 0:
        answer = f"You were {days} days old on the eve of the new millennium."
    else:
        answer = "You weren't born yet on the eve of the new millennium."

    return answer
    """


if True:
    day = input("Day: ")
    month = input("Month: ")
    year = input("Year: ")
else:
    day = "26"
    month = "06"
    year = "1991"

delta = how_old(day, month, year)   
if delta > 0:
    print(f"You were {delta} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")