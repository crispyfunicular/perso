# Write your solution here:
class Clock:    
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        # Up to 23:59:58 -> 23:59:59
        if self.seconds < 59:
            self.seconds += 1
        else:
            # 23:58:59 -> 23:59:00
            if self.minutes < 59 and self.seconds == 59:
                self.minutes += 1
                self.seconds = 0
            else:
                if self.hours < 23 and self.minutes == 59 and self.seconds == 59:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
                else:
                    if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
                        self.seconds = 0
                        self.minutes = 0
                        self.hours = 0


    def __str__(self):
        hour = f"{self.hours:02}"
        min = f"{self.minutes:02}"
        sec = f"{self.seconds:02}"

        return f"{hour}:{min}:{sec}"

    def set(self, hour: int, minutes: int):
        self.hours = hour
        self.minutes = minutes
        self.seconds = 0
