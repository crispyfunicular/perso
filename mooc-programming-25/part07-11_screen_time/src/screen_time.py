# Write your solution here
from datetime import datetime, timedelta

def compute_screen_time(input_time: str, duration: int, filename: str):    
    lines_lst = []
    total_minutes = 0
    start = datetime.strptime(input_time, "%d.%m.%Y")
    #print(start.strftime("%d.%m.%Y"))

    i = 0
    while i < duration:
        date_i = (start + timedelta(days=i)).strftime("%d.%m.%Y")
        screen_time = input(f"Screen time {date_i}: ").replace(" ", "/")
        lines_lst.append(f"{date_i}: {screen_time}")
        total_minutes += int(screen_time.split("/")[0]) + int(screen_time.split("/")[1]) + int(screen_time.split("/")[2])
        i += 1
        if i == duration:
            end = date_i
    
    with open(filename, "w") as my_file:
        my_file.write(f"Time period: {start.strftime("%d.%m.%Y")}-{end}\n")       
        my_file.write(f"Total minutes: {total_minutes}\n")       
        my_file.write(f"Average minutes: {total_minutes / duration}\n")
        for item in lines_lst:            
            my_file.write(item + "\n")
  

if True:        
    filename = input("Filename: ")
    input_time = input("Starting date: ")
    duration = int(input("How many days: "))
else:
    choice = int(input("choice: "))
    if choice == 1:
        filename = "late_june.txt"
        input_time = "24.6.2020"
        duration = 3
    elif choice == 2:
        filename = "first_of_may.txt"
        input_time = "1.5.2020"
        duration = 1

print("Please type in screen time in minutes on each day (TV computer mobile):")

compute_screen_time(input_time, duration, filename)
print("Data stored in file", filename)

