# Write your solution here

def check_weeks(week: str) -> bool:
    week_list = week.split(" ")
    try:
        week_nb = int(week_list[1])
        if not 0 < week_nb < 53:
            return False
    except ValueError:
        #print(f"The week number for {week} is incorrect.")
        return False
    return True


def check_numbers(week_numbers: str) -> bool:
    numbers_lst = week_numbers.split(",")
    numbers_check = []
    if len(numbers_lst) != 7:
        #raise ValueError(f"Too few numbers in {numbers_lst}.")
        #print(f"Too few/many numbers in {numbers_lst}.")
        return False
    for number in numbers_lst:
        try:
            int_nb = int(number)
            if not 0 < int_nb < 40:
                #raise ValueError(f"The week number {week} is incorrect.")
                #print(f"The number {int_nb} is not correct in {numbers_lst}.")
                return False
            if int_nb in numbers_check:
                #print(f"{int_nb} is written twice in {numbers_lst}")
                return False
            numbers_check.append(int_nb)                 
        except ValueError:
            #print(f"Number {number} is not correct in {numbers_lst}.")
            return False
    return True


def filter_incorrect():
    with open("correct_numbers.csv", "w") as my_file:   
        pass
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            week = parts[0]
            week_numbers = parts[1]

            if not check_weeks(week):
                continue
            if not check_numbers(week_numbers):
                continue
            with open("correct_numbers.csv", "a") as my_file:       
                my_file.write(f"{line}\n")


def main():
    filter_incorrect()
        

if __name__ == "__main__":
    main()
