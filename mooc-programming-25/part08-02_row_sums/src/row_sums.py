# Write your solution here

def row_sums(my_matrix: list):
    sum_l = 0
    for l in my_matrix:
        sum_l = sum(l)
        l.append(sum_l)


def main():
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
    #[[1, 2, 3], [3, 4, 7]]


if __name__ == "__main__":
    main()
