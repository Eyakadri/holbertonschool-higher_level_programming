#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num), end="$\n")
            else:
                print("{:d}".format(num), end=" ")
        if not row:
            print("$")
