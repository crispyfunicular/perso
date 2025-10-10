# Write your solution here
def even_numbers(beginning: int, maximum: int):
    number = beginning
    if number % 2 != 0:
        number += 1
    
    while number <= maximum:
        yield number
        number += 2


def main():
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
    
    print()

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)


if __name__ == "__main__":
    main()
