def square_matrix_simple(matrix):
    new = []
    for i in range(3):
        new.append([j ** 2 for j in matrix[i]])
    return new

