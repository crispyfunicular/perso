# Write your solution here
from string import digits
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    if len(pic) > 11:
        return False
    
    day = int(pic[:2])
    month = int(pic[2:4])
    year_yy = int(pic[4:6])
    century = pic[6]
    if century == "+":
        year_yyyy = 1800 + year_yy
    elif century == "-":
        year_yyyy = 1900 + year_yy
    elif century == "A":
        year_yyyy = 2000 + year_yy
    else:
        return False
    id1 = pic[7]
    id2 = pic[8]
    id3 = pic[9]
    control = pic[10]
    dob_id = int(pic[:6] + pic[7:10])
    remainder = dob_id % 31
    remainder_lst = "0123456789ABCDEFHJKLMNPRSTUVWXY"
        
    try:
        datetime(year_yyyy, month, day)
    except ValueError:
        return False
    
    if id1 not in digits:
        return False
    elif id2 not in digits:    
        return False
    elif id3 not in digits: 
        return False
    elif control != remainder_lst[remainder]:
        return False
    else:
        return True


def main():
    pic = "230827-906F"
    print(is_it_valid(pic))


if __name__ == "__main__":
    main()
