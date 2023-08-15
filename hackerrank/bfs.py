"""
Consider an undirected graph where each edge weighs 6 units. Each of the nodes is labeled consecutively from 1 to n.

You will be given a number of queries. For each query, you will be given a list of edges describing an undirected graph.
After you create a representation of the graph, you must determine and report the shortest distance to each of the other
nodes from a given starting position using the breadth-first search algorithm (BFS). Return an array of distances from
the start node in node number order. If a node is unreachable, return  for that node.

Example
The following graph is based on the listed inputs:

image

 // number of nodes
 // number of edges

 // starting node

All distances are from the start node . Outputs are calculated for distances to nodes  through : . Each edge is  units,
and the unreachable node  has the required return distance of .

Function Description

Complete the bfs function in the editor below. If a node is unreachable, its distance is .

bfs has the following parameter(s):

int n: the number of nodes
int m: the number of edges
int edges[m][2]: start and end nodes for edges
int s: the node to start traversals from
Returns
int[n-1]: the distances to nodes in increasing node number order, not including the start node
(-1 if a node is not reachable)
"""

from collections import defaultdict


def bfs(n, m, edges, s):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize distances array with -1 (unreachable)
    distances = [-1] * (n + 1)

    # Initialize the queue for BFS
    queue = [s]
    distances[s] = 0

    while queue:
        current_node = queue.pop(0)

        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:  # If not visited
                distances[neighbor] = distances[current_node] + 6
                queue.append(neighbor)

    # Exclude the starting node and return distances
    return distances[1:s] + distances[s + 1:]


def test_bfs():
    bfs(5, 3, [(1, 2), (1, 3), (3, 4)], 1)
