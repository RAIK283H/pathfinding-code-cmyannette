import math
import unittest
import pathing


class TestPathFinding(unittest.TestCase):

    def test_three_node_simple_graph_random(self):
        graph = [
            [(0, 0), [1]],
            [(0, 100), [0, 2]],
            [(0, 200), [1]]
        ]
        target_node = 1
        end_node = 2
        visited = set([])
        expected = [1, 2]
        path = []

        path_found = pathing.depth_traversal(graph, 0, target_node, end_node, visited, path, rand=True)
        path = path[1:]

        self.assertEqual(expected, path)
        self.assertTrue(path_found)
        self.assertTrue(target_node in path)

    def test_three_node_simple_graph_dfs(self):
        graph = [
            [(0, 0), [1]],
            [(0, 100), [0, 2]],
            [(0, 200), [1]]
        ]
        target_node = 1
        end_node = 2
        visited = set([])
        expected = [1, 2]
        path = []

        path_found = pathing.depth_traversal(graph, 0, target_node, end_node, visited, path, rand=False)
        path = path[1:]

        self.assertEqual(expected, path)
        self.assertTrue(path_found)
        self.assertTrue(target_node in path)

    def test_three_node_simple_graph_bfs(self):
        graph = [
            [(0, 0), [1]],
            [(0, 100), [0, 2]],
            [(0, 200), [1]]
        ]
        target_node = 1
        end_node = 2
        expected = [1, 2]

        path = pathing.breadth_traversal(graph, 0, target_node)[1:] + pathing.breadth_traversal(graph, target_node, end_node)[1:]

        self.assertEqual(expected, path)
        self.assertTrue(target_node in path)

    def test_ten_node_graph_dfs(self):
        graph = [
            [(0, 100), [1, 4, 6]],
            [(0, 200), [0, 2]],
            [(100, 200), [1, 3, 4]],
            [(200, 200), [2, 5, 9]],
            [(100, 100), [0, 2, 5, 7]],
            [(200, 100), [3, 4, 8, 9]],
            [(0, 0), [0, 7]],
            [(100, 0), [4, 6, 8]],
            [(200, 0), [5, 7, 9]],
            [(300, 100), [3, 5, 8]]
        ]
        target_node = 3
        end_node = 9
        expected = [1, 2, 3, 5, 4, 7, 8, 9]
        visited = set([])
        path = []

        pathing.depth_traversal(graph, 0, target_node, end_node, visited, path, rand=False)
        path = path[1:]

        self.assertEqual(expected, path)
        self.assertTrue(target_node in path)

    def test_ten_node_graph_bfs(self):
        graph = [
            [(0, 100), [1, 4, 6]],
            [(0, 200), [0, 2]],
            [(100, 200), [1, 3, 4]],
            [(200, 200), [2, 5, 9]],
            [(100, 100), [0, 2, 5, 7]],
            [(200, 100), [3, 4, 8, 9]],
            [(0, 0), [0, 7]],
            [(100, 0), [4, 6, 8]],
            [(200, 0), [5, 7, 9]],
            [(300, 100), [3, 5, 8]]
        ]
        target_node = 3
        end_node = 9
        expected = [1, 2, 3, 9]

        path = pathing.breadth_traversal(graph, 0, target_node)[1:] + pathing.breadth_traversal(graph, target_node, end_node)[1:]

        self.assertEqual(expected, path)
        self.assertTrue(target_node in path)

if __name__ == '__main__':
    unittest.main()
