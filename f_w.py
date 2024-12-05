import graph_data

# Convert adjacency list to a weighted matrix for a given graph
def adj_to_matrix(graph):
    # Initialize matrix with infinite weights for all values
    matrix = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]

    # Loop through each node
    for i, node in enumerate(graph):

        # Get node coords for distance/weight calculation
        coords = node[0]

        # Loop through adjacency list
        for adjacency in node[1]:

            # Get adjacent nodes' coords and calculate distance from current node
            adj_coords = graph[adjacency][0]
            weight = get_distance(coords, adj_coords)

            # Store weight in corresponding part of matrix
            matrix[i][adjacency] = weight
    
    return matrix

# Distance formula calculation
def get_distance(coord1, coord2):
    return (((coord2[0] - coord1[0]) ** 2) + ((coord2[1] - coord1[1]) ** 2)) ** 0.5

# Calculates all shortest paths
def floyd_warshall(matrix):
    
    # Calculate range of matrix and initialize path matrix as all None
    n = len(matrix)
    p_matrix = [[None for _ in range(n)] for _ in range(n)]
    
    # Floyd-Warshall calculation
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    p_matrix[i][j] = k
    
    return matrix, p_matrix


# Use the path matrix and a given start and end node to find shortest path
def find_floyd_warshall_path(p_matrix, start, finish):
    path = []
    z = p_matrix[start][finish]

    # Build path until z is none
    while z is not None:
        path.insert(0, z)
        z = p_matrix[start][z]
    
    # Insert start and finish nodes to path and return
    path.insert(0, start)
    path.append(finish)
    return path

def main():
    graph = graph_data.graph_data[2]

    matrix = adj_to_matrix(graph)

    _, p_matrix = floyd_warshall(matrix)
    path = find_floyd_warshall_path(p_matrix, 0, len(graph) - 1)
    print(path)

if __name__ == "__main__":
    main()