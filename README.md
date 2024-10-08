### Customer Requirements
1. The Random player shall have a randomly assigned path which begins with the start node, ends with the exit node, and hits the target along the path. The path shall be a valid traversal such that each sequential pair of nodes in the path are connected by an edge.
    * The random pathing algorithm finds a path from the start node to the exit node visiting any given node at most once and going through the target node. It does so by recursively stepping into a node, shuffling its adjacencies, then stepping through each adjacency until a path to the end is found (including the target node). This algorithm cannot return to the start node and will not preemptively travel through the end node.

2. The players shall receive another statistic to be tracked on the scoreboard
    * The added statistic is a "nodes Visited" counter that actively tracks the amount of nodes visited during traversal.

