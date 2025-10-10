# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.people_lst = []
        self.combined_height = 0

    def add(self, person: Person):
        self.people_lst.append(person)
        self.combined_height += person.height

    def is_empty(self) -> bool:
        return len(self.people_lst) == 0

    def print_contents(self):
        print(f"There are {len(self.people_lst)} persons in the room, and their combined height is {self.combined_height} cm")
        for person in self.people_lst:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        min = 300
        if len(self.people_lst) != 0:
            for person in self.people_lst:
                if person.height < min:
                    min = person.height
                    shortest = person           
            return shortest
        return None
    
    def remove_shortest(self):
        shortest = self.shortest()
        if self.shortest() != None:
            self.people_lst.remove(shortest)
            self.combined_height -= shortest.height
            return shortest
        return None


def main():
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()


if __name__ == "__main__":
    main()