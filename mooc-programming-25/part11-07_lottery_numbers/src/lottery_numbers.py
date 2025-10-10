# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_number: int, lottery_numbers: list):
        self.week_number = week_number
        self.lottery_numbers = lottery_numbers

    def number_of_hits(self, numbers: list) -> int:
        return len([self.number for self.number in self.lottery_numbers if self.number in numbers])

    def hits_in_place(self, numbers) -> list:
        return [number if number in self.lottery_numbers else -1 for number in numbers]


def main():
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))


if __name__ == "__main__":
    main()