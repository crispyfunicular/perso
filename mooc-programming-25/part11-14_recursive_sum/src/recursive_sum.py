# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    # if the number is 1, there is nothing else to add
    if number <= 1:
        return number

    return number + recursive_sum(number-1)


def main():
    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))


if __name__ == "__main__":
    main()

