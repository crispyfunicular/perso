class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

    #def __repr__(self):
        #return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def by_name(attempt: CourseAttempt) -> str:
    return attempt.student_name


def accepted(attempts: list) -> list[CourseAttempt]:
    return list(filter(lambda attempt : attempt.grade >= 1, attempts))


def attempts_with_grade(attempts: list, grade: int) -> list[CourseAttempt]:
    return list(filter(lambda attempt : attempt.grade == grade, attempts))


def passed_students(attempts: list, course: str) -> list:    
    lst = list(filter(lambda attempt : attempt.course_name == course and attempt.grade > 0, attempts))
    lst_sorted = sorted(list(map(by_name, lst)))
    return lst_sorted

