import unittest
from Graph import Graph
from Graph import Node


class NodeTests(unittest.TestCase):

    def test_init(self):
        self.node = Node("test_node")
        self.assertEqual("test_node", self.node.name)
        self.assertEqual([], self.node.neighbors)


class GraphTests(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.node1 = Node("N1")
        self.node2 = Node("N2")
        self.node3 = Node("N3")

    def test_init(self):
        self.assertEqual([], self.graph.nodes)

    def test_add_edge(self):
        self.graph.add_edge(self.node1, self.node2)
        self.assertEqual([], self.graph.get_neighbors_for(self.node2))
        self.assertEqual([self.node2],
                         self.graph.get_neighbors_for(self.node1))

    def test_add_edge_no_nodes(self):
        self.graph.add_edge(self.node1, self.node2)
        self.assertEqual([self.node1, self.node2], self.graph.nodes)

    def test_get_neighbors_for(self):
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node1, self.node3)
        self.assertEqual([self.node1, self.node2, self.node3],
                         self.graph.nodes)

    def test_path_between(self):
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.assertTrue(self.graph.path_between(self.node1, self.node3))
        self.assertFalse(self.graph.path_between(self.node2, self.node1))

    def test_path_between_cyles(self):
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.graph.add_edge(self.node3, self.node1)
        self.assertTrue(self.graph.path_between(self.node2, self.node1))

    def test_str(self):
        self.graph.add_edge(self.node1, self.node2)
        self.graph.add_edge(self.node2, self.node3)
        self.graph.add_edge(self.node3, self.node1)
        print(self.graph)

if __name__ == '__main__':
    unittest.main()

# dictionary***; set...
