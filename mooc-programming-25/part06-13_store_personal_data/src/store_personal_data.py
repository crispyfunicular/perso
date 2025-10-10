# Write your solution here

def store_personal_data(person: tuple):
    #print(person)
    name = person[0]
    age = str(person[1])
    height = str(person[2])
    line = (name, age, height)
    line = ";".join(line)
    with open("people.csv", "a") as my_file:
        my_file.write(line + "\n")
    
    
def main():
    tuple = ("Paul Paulson", 37, 175.5)
    store_personal_data(tuple)


if __name__ == "__main__":
    main()
