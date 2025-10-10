# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    row_check = []
    """
    for i in row:
        row_check.append(i)
    row_check.sort()
    #print(row_check)
    if row_check != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
    return True
    """
    for i in row:
        if i in row_check:
            return False
        if i != 0:
            row_check.append(i)
    return True



def main():
    sudoku = [
        #[9, 7, 8, 6, 4, 5, 3, 1, 2],
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))


if __name__ == "__main__":
    main()
