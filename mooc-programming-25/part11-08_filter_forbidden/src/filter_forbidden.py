# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([character for character in string if character not in forbidden])


def main():
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)


if __name__ == "__main__":
    main()
