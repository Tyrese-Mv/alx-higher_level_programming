#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        for i, num in enumerate(_list):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print("")
