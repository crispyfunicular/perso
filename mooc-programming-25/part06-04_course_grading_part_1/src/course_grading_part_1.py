# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students_dict = {}
exercises_dict = {}


with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            students_dict[parts[0]] = (parts[1], parts[2])
#print(students_dict)


"""
for id in students_dict:
    print(students_dict[id])
    print(students_dict[id][0])
    print(students_dict[id][1])
"""


with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            exercises_dict[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
#print(exercises_dict)


for id in students_dict:
    if id in exercises_dict:
        print(students_dict[id][0], students_dict[id][1], exercises_dict[id])
    else:
        raise Exception(f"{id} unfound")
