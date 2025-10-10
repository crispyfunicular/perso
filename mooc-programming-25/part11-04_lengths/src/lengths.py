# WRITE YOUR SOLUTION HERE:
def lengths(lists: list) -> list:
    return [len(list) for list in lists]


def main():
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))


if __name__ == "__main__":
    main()