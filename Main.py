import Node
from Astar import *
import numpy as np


def create_matrix(row, col, block_list=[]):
    matrix = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(Node.Node(i, j))
        matrix.append(row)

    for block in block_list:
        matrix[block[0]][block[1]].block = True

    return matrix


def main():
    blocks = [[2, 2], [2, 3], [2, 4], [1, 4]]
    matrix = create_matrix(10, 10, blocks)

    start = matrix[1][3]
    target = matrix[5][4]
    a_star = Astar(matrix, start, target)
    path = a_star.find_path()


if __name__ == "__main__":
    main()
