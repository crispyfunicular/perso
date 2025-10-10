# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("name is an empty string")
    elif " " not in name:
        raise ValueError("name must contain two words")
    elif len(name) > 40:
        raise ValueError("name is too long")
    elif age < 0 or age > 150:
        raise ValueError("age")
    else:
        return (name, age)


def main():
    if False:
        name_input = input("Name: ")
        age_input = int(input("Age: "))
    else:
        name_input = "John Doe"
        age_input = 50
    
    (name, age) = new_person(name_input, age_input)
        

if __name__ == "__main__":
    main()
