import math
import unittest
import pathing
import hamiltonian_main
import permutation


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

    def test_small_hamiltonian_graph(self):
        graph = [
            [(0, 0), [1]],
            [(50, 50), [0, 2, 3]],
            [(100, 50), [1, 3]],
            [(50, 100), [1, 2, 4]],
            [(100, 100), [3]],
        ]

        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual = hamiltonian_main.find_hamiltonian_cycles(graph)
        
        assert expected == actual

    def test_small_nonhamiltonian_graph(self):
        graph = [
            [(0, 0), [1]],
            [(50, 50), [0, 2, 3]],
            [(100, 50), [1, 4]],
            [(50, 100), [1, 4]],
            [(100, 100), [3]],
        ]

        expected = []
        actual = hamiltonian_main.find_hamiltonian_cycles(graph)
        
        assert expected == actual

    def test_small_hamiltonian_graph_with_isolated_node(self):
        graph = [
            [(0, 0), [1]],
            [(50, 50), [0, 2, 3]],
            [(100, 50), [1, 3]],
            [(50, 100), [1, 2, 4]],
            [(150, 100), [3]],
            [(100, 100), [3]],
        ]

        expected = []
        actual = hamiltonian_main.find_hamiltonian_cycles(graph)
        
        assert expected == actual

    def test_three_input_permutations(self):
        input = [1, 2, 3]

        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        actual = permutation.generate_permutations(input)

        assert expected == actual

    def test_one_input_permutations(self):
        input = [1]

        expected = [[1]]
        actual = permutation.generate_permutations(input)

        assert expected == actual
    
    def test_five_input_permutations(self):
        input = [1, 2, 3, 4, 5]

        expected = [[1, 2, 3, 4, 5], [1, 2, 3, 5, 4], [1, 2, 5, 3, 4], [1, 5, 2, 3, 4], [5, 1, 2, 3, 4], [5, 1, 2, 4, 3],
                    [1, 5, 2, 4, 3], [1, 2, 5, 4, 3], [1, 2, 4, 5, 3], [1, 2, 4, 3, 5], [1, 4, 2, 3, 5], [1, 4, 2, 5, 3],
                    [1, 4, 5, 2, 3], [1, 5, 4, 2, 3], [5, 1, 4, 2, 3], [5, 4, 1, 2, 3], [4, 5, 1, 2, 3], [4, 1, 5, 2, 3],
                    [4, 1, 2, 5, 3], [4, 1, 2, 3, 5], [4, 1, 3, 2, 5], [4, 1, 3, 5, 2], [4, 1, 5, 3, 2], [4, 5, 1, 3, 2],
                    [5, 4, 1, 3, 2], [5, 1, 4, 3, 2], [1, 5, 4, 3, 2], [1, 4, 5, 3, 2], [1, 4, 3, 5, 2], [1, 4, 3, 2, 5],
                    [1, 3, 4, 2, 5], [1, 3, 4, 5, 2], [1, 3, 5, 4, 2], [1, 5, 3, 4, 2], [5, 1, 3, 4, 2], [5, 1, 3, 2, 4],
                    [1, 5, 3, 2, 4], [1, 3, 5, 2, 4], [1, 3, 2, 5, 4], [1, 3, 2, 4, 5], [3, 1, 2, 4, 5], [3, 1, 2, 5, 4],
                    [3, 1, 5, 2, 4], [3, 5, 1, 2, 4], [5, 3, 1, 2, 4], [5, 3, 1, 4, 2], [3, 5, 1, 4, 2], [3, 1, 5, 4, 2],
                    [3, 1, 4, 5, 2], [3, 1, 4, 2, 5], [3, 4, 1, 2, 5], [3, 4, 1, 5, 2], [3, 4, 5, 1, 2], [3, 5, 4, 1, 2],
                    [5, 3, 4, 1, 2], [5, 4, 3, 1, 2], [4, 5, 3, 1, 2], [4, 3, 5, 1, 2], [4, 3, 1, 5, 2], [4, 3, 1, 2, 5],
                    [4, 3, 2, 1, 5], [4, 3, 2, 5, 1], [4, 3, 5, 2, 1], [4, 5, 3, 2, 1], [5, 4, 3, 2, 1], [5, 3, 4, 2, 1],
                    [3, 5, 4, 2, 1], [3, 4, 5, 2, 1], [3, 4, 2, 5, 1], [3, 4, 2, 1, 5], [3, 2, 4, 1, 5], [3, 2, 4, 5, 1],
                    [3, 2, 5, 4, 1], [3, 5, 2, 4, 1], [5, 3, 2, 4, 1], [5, 3, 2, 1, 4], [3, 5, 2, 1, 4], [3, 2, 5, 1, 4],
                    [3, 2, 1, 5, 4], [3, 2, 1, 4, 5], [2, 3, 1, 4, 5], [2, 3, 1, 5, 4], [2, 3, 5, 1, 4], [2, 5, 3, 1, 4],
                    [5, 2, 3, 1, 4], [5, 2, 3, 4, 1], [2, 5, 3, 4, 1], [2, 3, 5, 4, 1], [2, 3, 4, 5, 1], [2, 3, 4, 1, 5],
                    [2, 4, 3, 1, 5], [2, 4, 3, 5, 1], [2, 4, 5, 3, 1], [2, 5, 4, 3, 1], [5, 2, 4, 3, 1], [5, 4, 2, 3, 1],
                    [4, 5, 2, 3, 1], [4, 2, 5, 3, 1], [4, 2, 3, 5, 1], [4, 2, 3, 1, 5], [4, 2, 1, 3, 5], [4, 2, 1, 5, 3],
                    [4, 2, 5, 1, 3], [4, 5, 2, 1, 3], [5, 4, 2, 1, 3], [5, 2, 4, 1, 3], [2, 5, 4, 1, 3], [2, 4, 5, 1, 3],
                    [2, 4, 1, 5, 3], [2, 4, 1, 3, 5], [2, 1, 4, 3, 5], [2, 1, 4, 5, 3], [2, 1, 5, 4, 3], [2, 5, 1, 4, 3],
                    [5, 2, 1, 4, 3], [5, 2, 1, 3, 4], [2, 5, 1, 3, 4], [2, 1, 5, 3, 4], [2, 1, 3, 5, 4], [2, 1, 3, 4, 5]]
        actual = permutation.generate_permutations(input)
        
        assert expected == actual

    def test_dijkstras_simple_graph(self):
        graph = [
            [(0, 0), [1]],
            [(200, -200), [0, 2]],
            [(200, -400), [1]]
        ]

        expected = [1, 2]
        actual = pathing.dijkstra_traversal(graph, 0, 2)[1:]

        assert expected == actual

    def test_dijkstras_medium_graph(self):
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

        expected = [4, 5, 9]
        actual = pathing.dijkstra_traversal(graph, 0, 9)[1:]
        
        assert expected == actual

    def test_dijkstras_medium_graph_with_target(self):
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

        expected = [1, 2, 3, 9]
        actual = pathing.dijkstra_traversal(graph, 0, 2)[1:] + pathing.dijkstra_traversal(graph, 2, 9)[1:]
        
        assert expected == actual

if __name__ == '__main__':
    unittest.main()
