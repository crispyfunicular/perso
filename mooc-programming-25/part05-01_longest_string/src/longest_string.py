# Write your solution here
def longest(strings: list):
    longuest_word = ""

    for element in strings:
        if len(element) > len(longuest_word):
            longuest_word = element
    return longuest_word


def main():
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))


if __name__ == "__main__":
    main()
