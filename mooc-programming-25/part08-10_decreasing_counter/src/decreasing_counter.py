# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("initial:", self.initial_value)
        print("value:", self.value)
        print("diff:", self.value - self.initial_value)
        

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    # Write the rest of the methods here!

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value


def main():
    counter = DecreasingCounter(55)
    
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()


if __name__ == "__main__":
    main()