from copy import deepcopy


class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __str__(self):
        neighbors = list(map(lambda x: x.name, deepcopy(self.neighbors)))
        return "{}: {}".format(self.name, neighbors)


class Graph:

    def __init__(self):
        self.nodes = []
        self.visited = []

    def add_edge(self, node_a, node_b):
        if node_a in self.nodes and node_b in self.nodes:
            if node_b not in node_a.neighbors:
                node_a.neighbors.append(node_b)
        elif node_a in self.nodes:
            node_a.neighbors.append(node_b)
            self.nodes.append(node_b)
        elif node_b in self.nodes:
            self.nodes.append(node_a)
            node_a.neighbors.append(node_b)
        else:
            self.nodes.append(node_a)
            self.nodes.append(node_b)
            node_a.neighbors.append(node_b)

    def get_neighbors_for(self, node):
        return node.neighbors

    def path_between(self, node_a, node_b):
        if node_a in self.nodes and node_a not in self.visited:
            self.visited.append(node_a)
            if node_b in node_a.neighbors:
                return True
            else:
                flag = False
                for neighbor in node_a.neighbors:
                    flag = flag or self.path_between(neighbor, node_b)
                return flag
        else:
            return False

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += "\n{}".format(node)
        return string
