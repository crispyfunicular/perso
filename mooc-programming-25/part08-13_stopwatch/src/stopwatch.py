# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        else:
            if self.minutes < 59:
                self.minutes += 1
                self.seconds = 0
            if self.minutes == 59 and self.seconds == 59:
                self.seconds = 0
                self.minutes = 0

    def __str__(self):
        min = f"{self.minutes:02}"
        sec = f"{self.seconds:02}"
        return f"{min}:{sec}"

