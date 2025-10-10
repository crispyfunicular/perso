# Write your solution here
from datetime import datetime, timedelta

def cheaters():
    max_dict = {}
    sub_dict = {}
    cheat_lst = []

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
            sub_time = datetime.strptime(parts[3], "%H:%M")
            if stud_name not in sub_dict:
                sub_dict[stud_name] = sub_time
            else:
                if sub_time > sub_dict[stud_name]:
                    sub_dict[stud_name] = sub_time
    
    for student in max_dict:
        if max_dict[student] < sub_dict[student]:
            cheat_lst.append(student) 
    #print(cheat_lst)

    return cheat_lst


def main():
    start_times = "start_times.csv"
    submissions = "submissions.csv"
    cheaters(start_times, submissions)


if __name__ == "__main__":
    main()
