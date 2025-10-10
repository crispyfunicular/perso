# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]

    for element in numbers:
        if element < smallest:
            smallest = element
    numbers.remove(smallest)


def main():
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)


if __name__ == "__main__":
    main()
