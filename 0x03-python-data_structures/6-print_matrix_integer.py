#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print("{:d}".format(matrix[row][column]), end="")
            if column != (len(matrix[row]) - 1):
                print(" ", end="")
        print("")
