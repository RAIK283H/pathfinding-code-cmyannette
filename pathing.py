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

target_node = None
random_path = []

def get_random_path():
    
    global target_node
    global random_path

    # Initialize nodes of interest for current graph
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Preconditions
    assert target_node != None, "Target node cannot be None!"
    assert end_node != None, "End node cannot be None!"
    assert graph_data.graph_data[global_game_data.current_graph_index][0] != None, "Start node cannot be None!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][0][1]) > 0, "Start node must have at least one adjacency!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][end_node][1]) > 0, "End node must have at least one adjacency!"

    # Reset path and visited trackers for graph
    random_path = []
    visited = []

    # Add path nodes to array to return
    random_find_node(0, end_node, visited)

    # Postconditions
    assert target_node in random_path, "Target node must be in the randomly generated path!"
    assert random_path[-1] == end_node, "End node must be the last visited node!"

    # Return path created by function
    return random_path

# Recursive function that randomly finds a path from the start node to the exit node visiting any node only once and going through the target node
def random_find_node(current_node, end_node, visited):

    # Mark current node as visited
    visited.append(current_node)

    # Base case: if current node is the end node and the target node is in the path, return true
    if current_node == end_node:
        if target_node in visited:
            return True

    # Get adjacency list of current node
    adjacencies = graph_data.graph_data[global_game_data.current_graph_index][current_node][1].copy()
    
    # Remove each visited node from possible adjacencies to visit
    for node in visited:
        try: adjacencies.remove(node)
        except ValueError: pass

    # Shuffle adjacencies to randomize the order the adjacencies are traversed in
    random.shuffle(adjacencies)
    
    # Loop through each adjacency
    for node in adjacencies:

        # If a correct path is found, add the node to the path list and return True to add the previous node
        if random_find_node(node, end_node, visited):
            random_path.insert(0, node)
            return True
    
    # If no path found, remove node from visited and return False
    visited.pop()
    return False


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
