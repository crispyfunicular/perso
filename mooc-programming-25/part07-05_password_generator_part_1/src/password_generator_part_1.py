# Write your solution here
from string import ascii_lowercase
from random import choice

def generate_password(nb: int) -> str:
    password = ""

    for i in range(nb):
        password += choice(ascii_lowercase)

    return password


def main():
    for i in range(10):
        print(generate_password(8))
    

if __name__ == "__main__":
    main()
