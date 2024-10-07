import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

visited = []
target_node = None
def get_random_path():
    global visited
    global target_node

    # Initialize paths, visited, and nodes of interest
    start_to_target_path = []
    target_to_end_path = []
    visited = []
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Create a random path from the start node to the target node
    random_find_node(0, end_node, start_to_target_path)

    # Reset visited for the path from the target to the end node
    # visited = [0, start_to_target_path[-1]]
    # random_find_node(target_node, end_node, target_to_end_path, exclude_end_node=False)

    return start_to_target_path + target_to_end_path

def random_find_node(current_node, target, path, exclude_end_node=False):
    global visited

    visited.append(current_node)
    adjacencies = graph_data.graph_data[global_game_data.current_graph_index][current_node][1].copy()
    
    if exclude_end_node:
        try: adjacencies.remove(len(graph_data.graph_data[global_game_data.current_graph_index]) - 1)
        except ValueError: pass
    for node in visited:
        try: adjacencies.remove(node)
        except ValueError: pass

    random.shuffle(adjacencies)
    
    if current_node == target:
        if target_node in visited:
            return True
        else:
            return False
    
    for node in adjacencies:
        if random_find_node(node, target, path, exclude_end_node):
            path.insert(0, node)
            return True
        
    return False


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
