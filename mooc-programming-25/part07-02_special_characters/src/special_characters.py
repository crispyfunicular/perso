# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    letters_1 = ""
    punct_2 = ""
    other_3 = ""
    for letter in my_string:
        if letter in ascii_letters:
            letters_1 += letter
        elif letter in punctuation:
            punct_2 += letter
        else:
            other_3 += letter

    return letters_1, punct_2, other_3


def main():
    my_string = "Olé!!! Hey, are ümläüts wörking?"
    parts = separate_characters(my_string)
    print(parts[0])
    print(parts[1])
    print(parts[2])
    

if __name__ == "__main__":
    main()
