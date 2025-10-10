
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str) -> tuple:
        if name not in self.__persons:
            numbers = []
            address = None
        else:
            numbers = self.__persons[name]._numbers
            address = self.__persons[name]._address
        return (numbers, address)

    def get_name(self, number: str):
        for person in self.__persons:
            for num in self.__persons[person]:
                if number == num:
                    return person._name
        return None

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search_name(self):
        name = input("name: ")
        numbers, address = self.__phonebook.get_entry(name)
        #print(numbers)
        if numbers == []:
            print("number unknown")
        else:
            for number in numbers:
                print(number)
        if address == None:
            print("address unknown")
        else:
            print(address)

    def search_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name(number)
        if name == None:
            print("unknown number")
        print(name)       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search_name()
            elif command == "3":
                self.add_address()
            else:
                self.help()


class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None
    
    def name(self):
        return self._name

    def numbers(self):
        return self._numbers
    
    def address(self):
        return self._address

    def add_number(self, number):
        self._numbers.append(number)
    
    def add_address(self, address):
        self._address = address


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

