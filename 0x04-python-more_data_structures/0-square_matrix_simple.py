#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for line in matrix:
        squares.append([x**2 for x in line])
    return (squares)
