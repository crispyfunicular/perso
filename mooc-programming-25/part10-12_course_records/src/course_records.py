# tee ratkaisusi tänne

class Course:
    def __init__(self):
        self.__course = {}
    
    def add_course(self, name: str, grade, credits):
        grade = int(grade)
        credits = int(credits)
        if not name in self.__course:
            self.__course[name] = CourseData(grade, credits)
        else:
            self.__course[name].add_grade(grade)
            self.__course[name].add_credits(credits)
    
    def get_data(self, name):
        grade = 0
        credits = 0

        if name in self.__course:
            grade = self.__course[name].grade()
            credits = self.__course[name].credits()

        return (grade, credits)

    def get_total_data(self):
        total_courses = 0
        total_credits = 0
        total_grades = 0
        for course in self.__course:
            total_courses += 1
            total_credits += self.__course[course].credits()
            total_grades += self.__course[course].grade()
        return(total_courses, total_credits, total_grades)

    def get_all_grades(self):
        grade5 = 0
        grade4 = 0
        grade3 = 0
        grade2 = 0
        grade1 = 0

        for course in self.__course:
            if self.__course[course].grade() == 5:
                grade5 += 1
            if self.__course[course].grade() == 4:
                grade4 += 1
            if self.__course[course].grade() == 3:
                grade3 += 1
            if self.__course[course].grade() == 2:
                grade2 += 1
            if self.__course[course].grade() == 1:
                grade1 += 1
        
        return (grade5, grade4, grade3, grade2, grade1)


class CoursesApplication:
    def __init__(self):
        self.__course = Course()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        #self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                print("bye")
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search_course()
            elif command == "3":
                self.get_stats()
            else:
                self.help()
    
    def add_course(self):
        name = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        self.__course.add_course(name, grade, credits)

    def search_course(self):
        name = input("course: ")
        grade, credits = self.__course.get_data(name)
        if grade == 0 or credits == 0:
            print("no entry for this course")
        else:
            print(f"{name} ({credits} cr) grade {grade}")

    def get_stats(self):
        total_courses, total_credits, total_grade = self.__course.get_total_data()
        (grade5, grade4, grade3, grade2, grade1) = self.__course.get_all_grades()
        
        if total_courses != 0:
            mean = round((total_grade / total_courses), 1)
        
        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean", mean)
        print("grade distribution")
        print("5:", grade5 * "x")
        print("4:", grade4 * "x")
        print("3:", grade3 * "x")
        print("2:", grade2 * "x")
        print("1:", grade1 * "x")


class CourseData():
    def __init__(self, grade=0, credits=0):
        self._grade = grade
        self._credits = credits
    
    def grade(self):
        return self._grade
    
    def credits(self):
        return self._credits

    def add_grade(self, grade):
        if grade > self.grade():
            self._grade = grade
    
    def add_credits(self, credits):
        if not self.credits():
            self._credits = credits


application = CoursesApplication()
application.execute()