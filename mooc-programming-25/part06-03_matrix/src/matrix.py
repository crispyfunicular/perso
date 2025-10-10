# write your solution here
def helper():
    matrix = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")    

            #transforme les strings en integers
            row_int = []
            for nb in row:
                nb_int = int(nb)
                row_int.append(nb_int)
            matrix.append(row_int)
    return matrix

            
def matrix_sum():
    matrix = helper()
    sum = 0
    for row in matrix:
        for nb in row:
            sum += nb
    return sum


def row_sums():
    matrix = helper()
    sum_lst = []
    for row in matrix:
        sum_row = 0
        for nb in row:
            sum_row += nb
        sum_lst.append(sum_row)
    return sum_lst


def matrix_max():
    matrix = helper()
    max = 0
    for row in matrix:
        for nb in row:
            if nb > max:
                max = nb
    return max


def main():
    helper()
    sum = matrix_sum()
    print(sum)
    max = matrix_max()
    print(max)
    sum_lst = row_sums()    
    print(sum_lst)


if __name__ == "__main__":
    main()