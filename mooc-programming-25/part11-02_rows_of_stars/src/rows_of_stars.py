# WRITE YOUR SOLUTION HERE:
def rows_of_stars(numbers: list) -> list:
    return [number * "*" for number in numbers]


def main():
    rows = rows_of_stars([1,2,3,4])
    for row in rows:
        print(row)

    print()

    rows = rows_of_stars([4, 3, 2, 1, 10])
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()