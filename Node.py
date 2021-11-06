import numpy as np


class Node:
    def __init__(self, i, j, block=False, g=10**5):
        self.i = i
        self.j = j
        self.block = block
        self.point = np.array([i, j])
        self.parent = None
        self.g = g
        self.h = 0
        self.f = 0
