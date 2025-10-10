# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self) -> float:
        if self.count == 0:
            return 0.0
        return self.numbers / self.count

pipou = NumberStats()
even_nb = NumberStats()
odd_nb = NumberStats()

print("Please type in integer numbers:")

while True:
    input_nb = int(input(""))
    if input_nb != -1:
        pipou.add_number(input_nb)
        if input_nb % 2 == 0:
            even_nb.add_number(input_nb)
        else:
            odd_nb.add_number(input_nb)
    else:
        break

print("Sum of numbers:", pipou.get_sum())
print("Mean of numbers:", pipou.average())
print("Sum of even numbers:", even_nb.get_sum())
print("Sum of odd numbers:", odd_nb.get_sum())