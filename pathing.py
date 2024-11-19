import graph_data
import global_game_data
from numpy import random
from queue import PriorityQueue

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

def get_random_path():
    global random_path

    # Initialize current graph and nodes of interest
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Preconditions
    assert target_node != None, "Target node cannot be None!"
    assert end_node != None, "End node cannot be None!"
    assert graph_data.graph_data[global_game_data.current_graph_index][0] != None, "Start node cannot be None!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][0][1]) > 0, "Start node must have at least one adjacency!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][end_node][1]) > 0, "End node must have at least one adjacency!"

    # Reset path and visited trackers for graph (add end_node to prevent going to end before target)
    random_path = []
    visited = set([])

    # Do a random depth traversal to end node including target node
    depth_traversal(current_graph, 0, target_node, end_node, visited, random_path, rand=True)

    # Postconditions
    assert target_node in random_path, "Target node must be in the randomly generated path!"
    assert random_path[-1] == end_node, "End node must be the last visited node!"

    random_path = random_path[1:]
    # Return path created by function
    return random_path

# Recursive function that finds a path from the start node to the exit node (randomly or not) visiting any node only once and going through the target node
def depth_traversal(graph, current_node, target_node, end_node, visited, path, rand=False, skip_first=False):
    
    # Mark current node as visited and add to path
    visited.add(current_node)
    if not skip_first:
        path.append(current_node)

    # Base case: if current node is the end node and the target node is in the path, return true
    if current_node == end_node and target_node in path:
        return True

    # Get adjacency list of current node
    adjacencies = graph[current_node][1].copy()
    
    # Remove each visited node from possible adjacencies to visit
    for node in visited:
        try: adjacencies.remove(node)
        except ValueError: pass

    # If random, shuffle adjacencies to randomize the order they are traversed in, otherwise traverse in order
    if (rand):
        random.shuffle(adjacencies)
    
    # Loop through each adjacency
    for node in adjacencies:
        if node not in visited:

            # If a correct path is found return True
            if depth_traversal(graph, node, target_node, end_node, visited, path, rand=rand):
                return True
    
    # If no path found, remove node from visited and path and return False
    visited.remove(current_node)
    path.pop()
    return False

def get_dfs_path():
    global DFS_path

    # Initialize current graph and nodes of interest
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Preconditions
    assert target_node != None, "Target node cannot be None!"
    assert end_node != None, "End node cannot be None!"
    assert graph_data.graph_data[global_game_data.current_graph_index][0] != None, "Start node cannot be None!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][0][1]) > 0, "Start node must have at least one adjacency!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][end_node][1]) > 0, "End node must have at least one adjacency!"

    # Reset path and visited trackers for graph (add end_node to prevent going to end before target)
    DFS_path = []
    visited = set([])

    # Do a depth traversal to end node including target node
    depth_traversal(current_graph, 0, target_node, end_node, visited, DFS_path, rand=False)

    # Postconditions
    assert target_node in DFS_path, "Target node must be in the generated path!"
    assert DFS_path[-1] == end_node, "End node must be the last visited node!"
    for i in range(len(DFS_path) - 1):
        assert DFS_path[i + 1] in current_graph[DFS_path[i]][1], "Vertice does not exist!"

    DFS_path = DFS_path[1:]
    # Return path created by function
    return DFS_path

def get_bfs_path():
    global BFS_path

    # Initialize current graph and nodes of interest
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Preconditions
    assert target_node != None, "Target node cannot be None!"
    assert end_node != None, "End node cannot be None!"
    assert graph_data.graph_data[global_game_data.current_graph_index][0] != None, "Start node cannot be None!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][0][1]) > 0, "Start node must have at least one adjacency!"
    assert len(graph_data.graph_data[global_game_data.current_graph_index][end_node][1]) > 0, "End node must have at least one adjacency!"
    
    BFS_path = breadth_traversal(current_graph, 0, target_node)[1:] + breadth_traversal(current_graph, target_node, end_node)[1:]

    # Postconditions
    assert target_node in BFS_path, "Target node must be in the generated path!"
    assert BFS_path[-1] == end_node, "End node must be the last visited node!"
    for i in range(len(BFS_path) - 1):
        assert BFS_path[i + 1] in current_graph[BFS_path[i]][1], "Vertice does not exist!"

    return BFS_path


def breadth_traversal(graph, start_node, end_node):
    
    # Queue and visited for unvisited nodes to visit next
    queue = [start_node]
    visited = set([0, start_node])

    # Key is node and value is parent. Used for finding start node from target/end node
    parents = {start_node: None}

    # Path to return
    BFS_path = []

    # Loop while queue has values to visit
    while queue:

        # Get current node from front of queue and add to visited
        current_node = queue.pop(0)

        # If the current node is the end node, backtrack through parents until start is found, adding nodes to path
        if current_node == end_node:
            while current_node is not None:
                BFS_path.insert(0, current_node)
                current_node = parents[current_node]
            return BFS_path

        # Get current adjacencies
        adjacencies = graph[current_node][1].copy()

        # Add each unvisited adjacency to queue and visited
        for node in adjacencies:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                parents[node] = current_node
    
    return BFS_path


def get_dijkstra_path():

    # Initialize current graph and nodes of interest
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    end_node = len(graph_data.graph_data[global_game_data.current_graph_index]) - 1

    # Get path
    dijkstra_path = dijkstra_traversal(current_graph, 0, target_node) + dijkstra_traversal(current_graph, target_node, end_node)[1:]

    # Assertions
    assert dijkstra_path[0] == 0
    assert dijkstra_path[-1] == end_node
    for i in range(len(dijkstra_path) - 1):
        assert dijkstra_path[i + 1] in current_graph[dijkstra_path[i]][1], "Vertice does not exist!"

    return dijkstra_path[1:]

def dijkstra_traversal(graph, start_node, end_node):
    
    # Priority queue and related information about traversal
    queue = PriorityQueue()
    acc_cost = {}
    acc_cost[start_node] = 0
    queue.put((0, start_node))

    # Parents map to track nodes and their parents
    parents = {}
    parents[start_node] = None

    # While the queue still has values
    while not queue.empty():
        
        # Current node to work with
        current = queue.get()[1]

        # See if we've hit the end
        if current == end_node:
            break

        # Get neighbors and loop through each
        neighbors = graph[current][1].copy()
        for neighbor in neighbors:
            
            # Calculate updated cost
            new_cost = acc_cost[current] + get_distance(graph, current, neighbor)

            # Check if cell has been visited
            if neighbor not in acc_cost or new_cost < acc_cost[neighbor]:
                
                # Update parents, cost, and add to queue
                parents[neighbor] = current
                acc_cost[neighbor] = new_cost
                priority = new_cost
                queue.put((priority, neighbor))

    # Backtrack and build path if possible
    dijkstra_path = []
    current = end_node
    while current is not None:
        dijkstra_path.insert(0, current)
        current = parents[current]

    return dijkstra_path

def get_distance(graph, node1, node2):
    x1 = graph[node1][0][0]
    y1 = graph[node1][0][1]
    x2 = graph[node2][0][0]
    y2 = graph[node2][0][1]
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
