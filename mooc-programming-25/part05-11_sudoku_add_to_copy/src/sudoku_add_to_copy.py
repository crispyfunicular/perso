# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku2 = []
    for row in sudoku:
        sudoku2.append(row[:])
    sudoku2[row_no][column_no] = number
    return sudoku2


def print_sudoku(sudoku: list):
    count_row = 0
    for row in sudoku:
        count_col = 0
        for digit in row:
            if digit == 0:
                print("_ ", end="")
            else:
                print(digit, "", end="")
            count_col += 1
            if count_col == 3 or count_col == 6:
                print (" ", end="")
        print()
        count_row += 1
        if count_row == 3 or count_row == 6:
            print()


def main():
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    s = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 5, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    res = copy_and_add(s, 1, 1, 5)
    print()
    print("res:")
    print_sudoku(res)


if __name__ == "__main__":
    main()
