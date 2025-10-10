# Write your solution here
def add_student(database: dict, student: str):
    if student not in database:
            database[student] = {}
    return database


def add_course(database: dict, student: str, course: tuple):
    course_name = course[0]
    grade = course[1]
    if student in database and grade > 0:
        courses = database[student]
        if course_name not in courses or courses[course_name] < grade:
            courses[course_name] = grade
    return database


def print_student(database: dict, student: str):
    if student not in database:
        print(f"{student}: no such person in the database")
    elif not database[student]:
        print(f"{student}:")
        print(" no completed courses")
    else:
        sum_grades = 0
        print(f"{student}:")
        print(f" {len(database[student])} completed courses:")
        for course_name in database[student]:
            grade = database[student][course_name]
            print(" ", course_name, grade)
            sum_grades += grade
        print(" average grade", sum_grades/len(database[student]))


def summary(database):
    students_no = 0
    max_courses = 0
    max_courses_name = ""
    max_mean = 0
    max_mean_name = ""

    for student_name, courses in database.items():
        students_no += 1
        courses_no = 0
        sum_grades = 0
        for course_name, grade in courses.items():
            courses_no += 1
            sum_grades += grade
            mean = sum_grades / courses_no
            if mean > max_mean:
                max_mean = mean
                max_mean_name = student_name
        if courses_no > max_courses:
            max_courses = courses_no
            max_courses_name = student_name

    print("students", students_no)
    print("most courses completed", max_courses, max_courses_name)
    print("best average grade", max_mean, max_mean_name)


def main():
    print("* students1:")
    students1 = {}
    add_student(students1, "Peter")
    add_course(students1, "Peter", ("Introduction to Programming", 3))
    add_course(students1, "Peter", ("Advanced Course in Programming", 2))
    add_course(students1, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students1, "Peter", ("Introduction to Programming", 2))
    add_student(students1, "Eliza")
    print_student(students1, "Peter")
    print_student(students1, "Eliza")
    print_student(students1, "Jack")
    summary(students1)

    """
    print()
    print("* students2:")
    students2 = {}
    add_student(students2, "Emily")
    add_student(students2, "Peter")
    add_course(students2, "Emily", ("Introduction to Programming", 5))
    add_course(students2, "Emily", ("Introduction to Databases", 4))
    add_course(students2, "Peter", ("Data Structures and Algorithms", 3))
    print_student(students2, "Emily")
    summary(students2)

    print()
    print("* students3:")
    students3 = {}
    add_student(students3, "Emily")
    add_student(students3, "Peter")
    add_course(students3, "Emily", ("Software Development Methods", 4))
    add_course(students3, "Emily", ("Software Development Methods", 5))
    add_course(students3, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students3, "Peter", ("Models of Computation", 0))
    add_course(students3, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students3, "Peter", ("Introduction to Computer Science", 1))
    print_student(students3, "Emily")
    print_student(students3, "Peter")
    summary(students3)

    print()
    print("* students4:")
    students4 = {}
    add_student(students4, "Emily")
    add_student(students4, "Peter")
    add_course(students4, "Emily", ("Software Development Methods", 4))
    add_course(students4, "Emily", ("Software Development Methods", 5))
    add_course(students4, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students4, "Peter", ("Models of Computation", 0))
    add_course(students4, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students4, "Peter", ("Introduction to Computer Science", 1))
    add_course(students4, "Peter", ("Software Engineering", 3))
    summary(students4)
    """


if __name__ == "__main__":
    main()
