# Write your solution here
def oldest_person(people: list):
    oldest_dob = 2025
    oldest_name = ""
    for p in people:
        if p[1] < oldest_dob:
            oldest_name = p[0]
            oldest_dob = p[1]
    return oldest_name


def main():
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))


if __name__ == "__main__":
    main()
