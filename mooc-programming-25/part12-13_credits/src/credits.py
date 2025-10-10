from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits (courses: list[CourseAttempt]) -> int:
    #nb_credits = 0
    nb_credits = reduce(lambda reduced_sum, course: reduced_sum + course.credits, courses, 0)
    #for course in courses:
        #nb_credits += course.credits
    return nb_credits


def sum_of_passed_credits(courses: list[CourseAttempt]) -> int:
    passed_courses = filter(lambda course: course.grade > 0, courses)
    passed_credits = reduce(lambda reduced_sum, course: reduced_sum + course.credits, passed_courses, 0)
    return passed_credits


def average(courses: list[CourseAttempt]) -> float:
    passed_courses = list(filter(lambda course: course.grade > 0, courses))
    nb_courses = len(passed_courses)
    passed_grades = reduce(lambda reduced_sum, course: reduced_sum + course.grade, passed_courses, 0)
    return passed_grades / nb_courses

