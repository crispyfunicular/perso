# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        names = self.name.split(" ")
        return names[0]

    def return_last_name(self):
        names = self.name.split(" ")
        return names[1]


def main():
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())


if __name__ == "__main__":
    main()
