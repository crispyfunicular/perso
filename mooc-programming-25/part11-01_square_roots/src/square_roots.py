# WRITE YOUR SOLUTION HERE:
from math import sqrt

def square_roots(numbers: list) -> list:
    return [sqrt(number) for number in numbers]    


def main():
    lines = square_roots([1,2,3,4])
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()