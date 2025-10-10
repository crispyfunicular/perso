# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date

def list_years(dates: list) -> list:
    list1 = []
    list2 = []

    for d in dates:
        list1.append(d.year)
        
    i = len(list1)    
    while i > 0:
        min_y = 3000
        for y in list1:
            if y < min_y:
                min_y = y
        list1.remove(min_y)
        list2.append(min_y)
        i -= 1
    
    return list2


def main():
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
    #[1993, 2006, 2019]


if __name__ == "__main__":
    main()
