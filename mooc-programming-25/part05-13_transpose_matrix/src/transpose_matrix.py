# Write your solution here
def transpose(matrix: list):
    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        for row in matrix:
            new_matrix[i].append(row[i])    
    
    for i in range(len(matrix)):
        for row in matrix:
            matrix[i] = new_matrix[i]


def main():
    maatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriix = [[1, 2], [1, 2]]
    print(transpose(maatrix))
    print(transpose(matriix))


if __name__ == "__main__":
    main()
