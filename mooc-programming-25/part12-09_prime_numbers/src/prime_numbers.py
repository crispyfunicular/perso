# Write your solution here
def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1


def accepted(attempts: list):
    pass


s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

for attempt in accepted([s1, s2, s3]):
    print(attempt)