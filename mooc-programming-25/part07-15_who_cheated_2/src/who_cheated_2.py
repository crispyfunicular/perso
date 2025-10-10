# Write your solution here
from datetime import datetime, timedelta


def final_points() -> dict:
    max_dict = {}
    grades = {}
    total_points = {}

    with open("start_times.csv") as my_file:        
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
            max_dict[parts[0]] = datetime.strptime(parts[1], "%H:%M") + timedelta(hours=3)

    with open("submissions.csv") as my_file:        
        for line in my_file:
            line = line.strip()
            parts = line.split(";")
            stud_name = parts[0]
            task = parts[1]
            points = int(parts[2])
            sub_time = datetime.strptime(parts[3], "%H:%M") 

            if stud_name not in grades:
                stud_gra = {
                    "1" : 0,
                    "2" : 0,
                    "3" : 0,
                    "4" : 0,
                    "5" : 0,
                    "6" : 0,
                    "7" : 0,
                    "8" : 0,
                }
                total_points[stud_name] = 0
            
            if points > grades[stud_name][task]:
                if sub_time < max_dict[stud_name]:
                    grades[stud_name][task] = points

        for student in grades:
            for exo in grades[student]:
                total_points[student] += grades[student][exo]

    #print(max_dict)
    #print()
    print(total_points)
    
    return total_points


def main():
    final_points()


if __name__ == "__main__":
    main()
