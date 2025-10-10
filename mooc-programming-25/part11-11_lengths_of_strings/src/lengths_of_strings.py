# WRITE YOUR SOLUTION HERE:
def lengths(strings: list) -> dict:
    return {string : len(string) for string in strings}


def main():
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)


if __name__ == "__main__":
    main()
