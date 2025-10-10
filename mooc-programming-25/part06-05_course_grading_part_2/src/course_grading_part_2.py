# write your solution here
import math

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

students_dict = {}
exercises_dict = {}
exam_dict = {}
grades_dict = {}
grade = 0


with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            students_dict[parts[0]] = (parts[1], parts[2])
#print(students_dict)


with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            exercises_done = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
            #print("exercises done:", exercises_done)
            percentage_exercises = (exercises_done / 40) * 10
            exercises_points = math.trunc(percentage_exercises)
            exercises_dict[parts[0]] = exercises_points
            #print("exercises points:", exercises_points)


with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            examination_points = int(parts[1]) + int(parts[2]) + int(parts[3])
            total_points = exercises_dict[parts[0]] + examination_points
            #print("total points:", total_points)

            if total_points > 27:
                grade = 5
            elif total_points > 23:
                grade = 4
            elif total_points > 20:
                grade = 3
            elif total_points > 17:
                grade = 2
            elif total_points > 14:
                grade = 1
            else:
                grade = 0
            #print("grade:", grade)

            grades_dict[parts[0]] = grade  


for id in students_dict:
    if id in exercises_dict:
        print(students_dict[id][0], students_dict[id][1], grades_dict[id])
    else:
        raise Exception(f"{id} unfound")
