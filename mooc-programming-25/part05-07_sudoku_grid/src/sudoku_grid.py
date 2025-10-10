# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for row in sudoku:
        check = []
        for digit in row:
            if digit in check:
                return False
            if digit != 0:
                check.append(digit)
    
    for column in range(9):
        check = []
        for row in sudoku:
            digit = row[column]
            if digit in check:
                return False
            if digit != 0:        
                check.append(row[column])
        
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            check = []
            for k in range(3):
                for l in range(3):
                    value = sudoku[i+k][j+l]
                    if value in check:
                        return False
                    if value != 0:
                        check.append(value)
                    #print(check)

    return True



def main():
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))


if __name__ == "__main__":
    main()
