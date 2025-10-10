# write your solution here


def read_fruits():
    dic_fruit = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])
            dic_fruit[name] = price

    return dic_fruit


def main():
    read_fruits()    

if __name__ == "__main__":
    main()