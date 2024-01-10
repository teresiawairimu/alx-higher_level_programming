#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for x in matrix:
        row = []
        for i in x:
            row.append(i**2)
        result.append(row)
    return result
