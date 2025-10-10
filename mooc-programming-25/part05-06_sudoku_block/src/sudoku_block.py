# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    block_check = []
    for i in range(3):
        for j in range(3):
            value = sudoku[row_no + i][column_no + j]
            if value in block_check:
                return False
            if value != 0:
                block_check.append(value)
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))


if __name__ == "__main__":
    main()
