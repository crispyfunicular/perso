# Write your solution here
from math import sqrt

def hypotenuse(leg1: float, leg2: float) -> int:
    h = sqrt(leg1 * leg1 + leg2 * leg2)
    return h


def main():
    leg1 = 3.0
    leg2 = 4.0
    h = hypotenuse(leg1, leg2)
    print(h)    


if __name__ == "__main__":
    main()
