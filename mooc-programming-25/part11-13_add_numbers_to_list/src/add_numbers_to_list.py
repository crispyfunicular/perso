# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        n = numbers[-1] + 1
        numbers.append(n)
        add_numbers_to_list(numbers)


def main():
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)


if __name__ == "__main__":
    main()

