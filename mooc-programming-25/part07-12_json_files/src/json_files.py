# Write your solution here
import json


def print_persons(filename: str):

    with open(filename) as my_file:
        data = my_file.read()
    people = json.loads(data)
    #print(people)
    for p in people:
        hobbies = f"({", ".join(p["hobbies"])})"
        print(p["name"], p["age"], "years", hobbies)


def main():
    filename = "file1.json"
    print_persons(filename)


if __name__ == "__main__":
    main()
