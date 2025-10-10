# Write your solution here
def create_tuple(x: int, y: int, z: int):
    lst = [x, y, z]
    min1 = min(lst)
    max2 = max(lst)
    sum3 = sum(lst)
    return (min1, max2, sum3)


def main():
    print(create_tuple(5, 3, -1))


if __name__ == "__main__":
    main()
