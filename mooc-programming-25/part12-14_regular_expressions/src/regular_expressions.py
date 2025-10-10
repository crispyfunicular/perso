# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in weekdays:
        if day in my_string:
            return True
    return False


def all_vowels(my_string: str) -> bool:
    #vowels = ["a", "e", "i", "o", "u"]
    #for letter in my_string:
        #if letter not in vowels:
            #return False
    #return True

    if re.search("^(a|e|i|o|u)+$", my_string):
        return True
    return False


def time_of_day(my_string: str):
    if re.search("^(((0|1)[0-9])|(2[0-3])):([0-5][0-9]):([0-5][0-9])$", my_string):
        return True
    return False

