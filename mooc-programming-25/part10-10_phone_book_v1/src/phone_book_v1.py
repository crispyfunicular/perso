# WRITE YOUR SOLUTION HERE:
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
        
    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def get_name(self, number: str):
        for person in self.__persons:
            for num in self.__persons[person]:
                if number == num:
                    return person
        return None
    
    def all_entries(self):
        return self.__persons

    def get_entry(self, name):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()
    

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # add the names and numbers from the file to the phone book
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    #def add_entry(self):
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
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def search_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name(number)
        if name == None:
            print("unknown number")
        print(name)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                #self.add_entry()
                self.add_number()
            elif command == "2":
                self.search_name()
            elif command == "3":
                #self.search_number()
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



application = PhoneBookApplication()
application.execute()
