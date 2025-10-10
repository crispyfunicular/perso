# Write your solution here
def get_str_numbers(number):
    units = {
        "0" : "zero",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine"
    }

    teens = {
        "10" : "ten",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "15" : "fifteen"
    }

    dizens = {
        "2" : "twen",
        "3" : "thir",
        "4" : "for",
        "5" : "fif",
        "6" : "six",
        "7" : "seven",
        "8" : "eigh",
        "9" : "nine"
    }

    if number < 10:
        unit = str(number)
    
    else:    
        unit = str(number)[1]
        dizen = str(number)[0]
        digit = dizen + unit
    
    if number < 10:
        written_number = units[unit]
    elif number < 16:
        written_number = teens[digit]
    elif number < 20:
        written_number = dizens[unit] + "teen"
    elif unit == "0":
        written_number =  dizens[dizen] + "ty"
    else:
        written_number = dizens[dizen] + "ty-" + units[unit]
    #print(written_number)
    
    return written_number


def dict_of_numbers():
    dict_numb = {}
    for i in range(0, 100):
        j = get_str_numbers(i)
        dict_numb[i] = j
    return dict_numb



def main():
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])


if __name__ == "__main__":
    main()
