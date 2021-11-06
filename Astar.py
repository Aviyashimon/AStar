import Node
import numpy as np


class Astar:
    def __init__(self, matrix, start_point, target_point):
        self.matrix = matrix
        self.start_point = start_point
        self.target_point = target_point
        self.open_list = [self.start_point]
        self.closed_list = []
        self.start_point.g = 0

    def find_minimum_f(self, nodes_list):
        minimum = nodes_list[0]
        for i in range(1, len(nodes_list)):
            if nodes_list[i].f < minimum.f:
                minimum = nodes_list[i]
        return minimum

    def final_path(self):
        return

    def get_neighbors(self, node, matrix):
        neighbors_list = []
        rowNumber0 = max(0, node.i - 1)
        colNumber0 = max(0, node.j - 1)
        rowNumber1 = min(node.i + 2, matrix.shape[0])
        colNumber1 = min(node.j + 2, matrix.shape[1])
        new_matrix = matrix[rowNumber0: rowNumber1, colNumber0:colNumber1]
        neighbors_list = list(new_matrix.reshape(-1))
        neighbors_list.remove(node)
        return neighbors_list

    def dist_between(self, first_node, second_node):
        if first_node.i != second_node.i and first_node.j != second_node.j:
            return 14
        else:
            return 10

    def heuristic_cost_estimate(self, node, target_point):
        dist = np.linalg.norm(node.point - target_point.point)
        return dist

    def find_path(self):

        while self.open_list:
            current_node = self.find_minimum_f(self.open_list)

            if current_node == self.target_point:
                self.print_final_matrix(self.final_path(current_node))
                return

            self.closed_list.append(current_node)
            self.open_list.remove(current_node)
            neighbors_list = self.get_neighbors(current_node, np.array(self.matrix))

            for neighbor in neighbors_list:
                tentative_g_score = current_node.g + self.dist_between(current_node, neighbor)
                if neighbor in self.closed_list or tentative_g_score >= neighbor.g:
                    continue
                if neighbor not in self.open_list or tentative_g_score < neighbor.g:
                    neighbor.parent = current_node
                    neighbor.g = tentative_g_score
                    neighbor.f = neighbor.g + self.heuristic_cost_estimate(neighbor, self.target_point)
                    if neighbor not in self.open_list and not neighbor.block:
                        self.open_list.append(neighbor)
        print("Path not found")
        return False

    def final_path(self, current):
        path = []
        while current != self.start_point:
            path.append(current)
            current = current.parent
        path.append(current)

        return path

    def print_final_matrix(self, final_path):
        print("S = Start point, E = End point, X = Block, V = Path")
        print()
        for i, row in enumerate(self.matrix):
            for j, node in enumerate(row):
                if node.block:
                    print("x", end="\t")
                elif node == self.start_point:
                    print("S", end="\t")
                elif node == self.target_point:
                    print("E", end="\t")
                elif node in final_path:
                    print("V", end="\t")
                else:
                    print(".", end="\t")
            print()
