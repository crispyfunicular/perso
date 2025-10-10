# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    count = 0

    def __init__ (self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = "NOT FINISHED"
        self.id = self.get_id()

    @classmethod
    def get_id(cls):
        cls.count += 1
        return cls.count

    def is_finished(self):
        return self.finished == "FINISHED"
    
    def mark_finished(self):
        self.finished = "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"


class OrderBook:
    def __init__(self):
        self.all_orders_lst = []

    def add_order(self, description: str, programmer: str, workload: int):
        order = Task(description, programmer, workload)
        self.all_orders_lst.append(order)

    def all_orders(self):
        return self.all_orders_lst

    def programmers(self):
        programmers_lst = set()
        for order in self.all_orders_lst:
            programmers_lst.add(order.programmer)
        return list(programmers_lst)
    
    def mark_finished(self, id: int):
        for order in self.all_orders_lst:
            if order.id == id:
                order.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self) -> list:
        return [order for order in self.all_orders_lst if order.finished == "FINISHED"]

    def unfinished_orders(self) -> list:
        return [order for order in self.all_orders_lst if order.finished == "NOT FINISHED"]

    def status_of_programmer(self, programmer: str) -> tuple:
        finished = 0
        unfinished = 0
        finished_hours = 0
        unfinished_hours = 0

        for order in self.all_orders_lst:
            if order.programmer == programmer:
                if order.finished == "FINISHED":
                    finished += 1
                    finished_hours += order.workload

                if order.finished == "NOT FINISHED":
                    unfinished += 1
                    unfinished_hours += order.workload
        
        if finished == 0 and unfinished == 0:
            raise ValueError

        return (finished, unfinished, finished_hours, unfinished_hours)


class OrderApplication:
    def __init__(self):
        self.__task = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status_programmer()
            else:
                self.help()

    # 1 add order
    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split(" ")
            self.__task.add_order(description, programmer, int(workload))
        except:
            print("erroneous input")
        
        print("added!")

    # 2 list finished tasks
    def list_finished_tasks(self):
        if self.__task.finished_orders() == []:
            print("no finished tasks")
        else:
            for order in self.__task.finished_orders():
                print(order)

    # 3 list unfinished tasks
    def list_unfinished_tasks(self):
        if self.__task.unfinished_orders() == []:
            print("no unfinished tasks")
        else:
            for order in self.__task.unfinished_orders():
                print(order)

    # 4 mark task as finished
    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.__task.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")
            
    # 5 programmers
    def list_programmers(self):
        if self.__task.programmers() == []:
            print("no programmer")
        else:
            for programmer in self.__task.programmers():
                print(programmer)

    # 6 status of programmer
    def status_programmer(self):
        programmer = input("programmer: ")
        try:
            (finished, unfinished, finished_hours, unfinished_hours) = self.__task.status_of_programmer(programmer)
            print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_hours} scheduled {unfinished_hours}")
        except:
            print("erroneous input")


# when testing, no code should be outside application except the following:
application = OrderApplication()
application.execute()
