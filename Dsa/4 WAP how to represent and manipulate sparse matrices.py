def create_sparse_matrix(matrix):
    sparse_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparse_matrix.append((i, j, matrix[i][j]))
    return sparse_matrix

def display_sparse_matrix(sparse_matrix):
    print("Row\tCol\tValue")
    for row, col, value in sparse_matrix:
        print(f"{row}\t{col}\t{value}")

# Example usage
matrix = [
    [0, 0, 3],
    [0, 4, 0],
    [0, 0, 0],
    [5, 0, 0]
]

sparse = create_sparse_matrix(matrix)
print("Sparse Matrix Representation:")

display_sparse_matrix(sparse)
