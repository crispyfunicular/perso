# Write your solution here
import math
import string

def change_case(orig_string: str) -> str:
    new_string = orig_string.swapcase()
    return new_string


def split_in_half(orig_string: str) -> tuple:
    length = math.floor(len(orig_string) / 2)
    slice1 = orig_string[:length]
    slice2 = orig_string[length:]
    return (slice1, slice2)


def remove_special_characters(orig_string: str) -> str:
    without_characters = ""
    for letter in orig_string:
        if letter.isalnum() or letter == " ":
            without_characters += letter
    return without_characters


def main():
    #orig_string = "Well hello there!"
    orig_string = "This is a test, lets see how it goes!!!11!"
    change_case(orig_string)
    split_in_half(orig_string)
    remove_special_characters(orig_string)



if __name__ == "__main__":
    main()
