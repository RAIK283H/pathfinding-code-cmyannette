import graph_data
import permutation

def find_hamiltonian_cycles(graph):

    # Create input list of nodes (1, 2, ..., n-1)
    nodes = list(range(1, len(graph) - 1))

    # Generate all permutations of given nodes
    permutations = permutation.generate_permutations(nodes)

    # Loop through each permutation to see if it's a valid solution
    valid_perms = []
    for perm in permutations:
        if is_valid_permutation(graph, perm):
            valid_perms.append(perm)

    return valid_perms

def is_valid_permutation(graph, perm):
    
    # Loop through numbers to ensure adjacent numbers are in each other's adjacency list
    for i in range(-1, len(perm) - 1):
        node = perm[i]
        adj_node = perm[i + 1]
        if adj_node not in graph[node][1]:
            return False
    return True

def main():

    # Initialize graphs that won't take forever to run
    graphs = [graph_data.graph_data[0], graph_data.graph_data[1], graph_data.graph_data[4], graph_data.graph_data[6], graph_data.graph_data[7], graph_data.graph_data[8]]
    
    for i in range(len(graphs)):
        perms = find_hamiltonian_cycles(graphs[i])
        print(f"\nGRAPH {i}:")
        if perms:
            for perm in perms:
                print(perm)
        else: print("NO CYCLES!")

if __name__ == "__main__":
    main()