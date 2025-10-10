# Write your solution here:

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

