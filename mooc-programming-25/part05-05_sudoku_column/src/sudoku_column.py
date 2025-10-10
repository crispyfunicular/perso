# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column_check = []
    for i in sudoku:
        if i[column_no] in column_check:
            return False
        if i[column_no] != 0:
            column_check.append(i[column_no])
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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))


if __name__ == "__main__":
    main()
