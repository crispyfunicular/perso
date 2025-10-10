# Write your solution here
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


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    row = sudoku[row_no]
    row[column_no] = number


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

    print_sudoku(sudoku)
    
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
    

if __name__ == "__main__":
    main()
