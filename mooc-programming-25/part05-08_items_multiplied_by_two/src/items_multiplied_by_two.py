# Write your solution here
def double_items(numbers: list):
    new_numbers = []
    for element in numbers:
        new_numbers.append(2 * element)
    return new_numbers


def main():
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

if __name__ == "__main__":
    main()
