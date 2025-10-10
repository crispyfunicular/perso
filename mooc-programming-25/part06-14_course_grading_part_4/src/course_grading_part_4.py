# tee ratkaisu tänne
import math

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercises = input("Exercises completed: ")
    exam_pts = input("Exam points: ")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercises = "exercises1.csv"
    exam_pts = "exam_points1.csv"
    course_info = "course1.txt"


students_dict = {}
exercises_dict = {}
exec_dict = {}
exam_dict = {}
grades_dict = {}
final_dict = {}
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


with open(exercises) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            # "exec_nbr"
            exercises_done = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])          
            #print("exercises done:", exercises_done)
            percentage_exercises = (exercises_done / 40) * 10
            exercises_points = math.trunc(percentage_exercises)
            exercises_dict[parts[0]] = exercises_points
            #print("exercises points:", exercises_points)
            exec_dict[parts[0]] = (exercises_done, exercises_points)


with open(exam_pts) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            examination_points = int(parts[1]) + int(parts[2]) + int(parts[3])
            total_points = exercises_dict[parts[0]] + examination_points
            exam_dict[parts[0]] = examination_points, total_points
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
        final_dict[id] = students_dict[id][0], students_dict[id][1], grades_dict[id]
    else:
        raise Exception(f"{id} unfound")

col1 = "name"
col2 = "exec_nbr"
col3 = "exec_pts."
col4 = "exm_pts."
col5 = "tot_pts."
col6 = "grade"
print(f"{col1:30}{col2:10}{col3:10}{col4:10}{col5:10}{col6:10}")
for id in students_dict:
    name = students_dict[id][0] + " " + students_dict[id][1]
    print(f"{name:30}{exec_dict[id][0]:<10}{exec_dict[id][1]:<10}{exam_dict[id][0]:<10}{exam_dict[id][1]:<10}{grades_dict[id]:<10}")



print("Results written to files results.txt and results.csv")
