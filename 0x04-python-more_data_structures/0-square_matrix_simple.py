#!/usr/bin/python3

res = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res[i][j] = (matrix[i][j]**2)

    return res
