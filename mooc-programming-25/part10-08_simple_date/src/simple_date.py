# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __lt__(self, another):
        if self.year < another.year:
            return True
        if self.year == another.year and self.month < another.month:
            return True
        if self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        else:
            return False

    def __gt__(self, another):
        if self.year > another.year:
            return True
        if self.year == another.year and self.month > another.month:
            return True
        if self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        else:
            return False

    def __eq__(self, another):
        return self.year == another.year and self.month == another.month and self.day == another.day

    def __ne__(self, another):        
        return self.year != another.year or self.month != another.month or self.day != another.day

    def __add__(self, days: int):
        all_days = self.day + days + self.month * 30 + self.year * 12 * 30
        add_year = all_days // (30*12)
        all_days -= add_year * (30*12)
        add_month = all_days // 30
        all_days -= add_month * 30
        add_day = all_days
        Total = SimpleDate(add_day, add_month, add_year)
        return Total
    
    def __sub__(self, another):
        all_days_self = self.day + self.month * 30 + self.year * 30 * 12
        all_days_another = another.day + another.month * 30 + another.year * 30 * 12
        diff_days = all_days_self - all_days_another
        if diff_days < 0:
            diff_days *= -1
        return diff_days


def main():
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)


if __name__ == "__main__":
    main()