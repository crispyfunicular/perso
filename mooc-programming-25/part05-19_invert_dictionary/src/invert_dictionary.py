# Write your solution here
def invert(dictionary: dict):
    dictionary2 = {}

    for key in dictionary:
        dictionary2[dictionary[key]] = key
    dictionary.clear()
    for key in dictionary2:
        dictionary[key] = dictionary2[key]


def main():
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)


if __name__ == "__main__":
    main()
