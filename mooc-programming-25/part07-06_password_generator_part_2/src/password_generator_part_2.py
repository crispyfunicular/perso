# Write your solution here
from string import ascii_lowercase
from random import choice


def generate_strong_password(nb: int, num: bool, punct: bool) -> str:
    lst = ascii_lowercase
    valid = False

    if num == True:
        lst += "0123456789"
    
    if punct == True:
        lst += "!?=+-()#"
    
    while not valid:
        password = ""
        for i in range(nb):
            password += choice(lst)    
        valid = check_password(password, num, punct)
    
    return password


def check_password(password: str, num: bool, punct: bool) -> bool:
    has_letter = False
    has_num = not num
    has_punct = not punct    
        
    for ch in password:
        if ch in ascii_lowercase:
            has_letter = True
        elif ch in "0123456789":
            has_num = True
        elif ch in "!?=+-()#":
            has_punct = True

    return has_letter and has_num and has_punct


def main():
    for i in range(10):
        print(generate_strong_password(8, True, True))


if __name__ == "__main__":
    main()
