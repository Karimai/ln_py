"""
https://www.codewars.com/kata/576986639772456f6f00030c/train/python

You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1]. Number of climb
rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

Location altitude is defined as an integer number (0-9).
"""
import heapq


def parse_grid(grid_string):
    rows = grid_string.strip().split('\n')
    grid = []
    for row in rows:
        grid.append([int(cell) for cell in row])
    return grid


def path_finder(area):
    grid = parse_grid(area)
    n = len(grid)

    # Create a graph representation
    graph = {}
    for i in range(n):
        for j in range(n):
            node = (i, j)
            neighbors = []
            # Check adjacent cells
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    neighbors.append((nx, ny))
            graph[node] = neighbors

    # Initialize distances to infinity
    distances = {node: float('inf') for node in graph}
    distances[(0, 0)] = 0

    # Priority queue to store nodes to be visited
    queue = [(0, (0, 0))]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # Check if we reached the target node
        if current_node == (n - 1, n - 1):
            return distances[current_node]

        # Skip if we have already found a shorter path to this node
        if current_dist > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor in graph[current_node]:
            nx, ny = neighbor
            new_dist = current_dist + abs(grid[nx][ny] - grid[current_node[0]][current_node[1]])
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    # If we reached here, there is no path to the target node
    return -1


def test_path_finder():
    a = "\n".join([
        "000",
        "000",
        "000"
    ])

    b = "\n".join([
        "010",
        "010",
        "010"
    ])

    c = "\n".join([
        "010",
        "101",
        "010"
    ])

    d = "\n".join([
        "0707",
        "7070",
        "0707",
        "7070"
    ])

    e = "\n".join([
        "700000",
        "077770",
        "077770",
        "077770",
        "077770",
        "000007"
    ])

    f = "\n".join([
        "777000",
        "007000",
        "007000",
        "007000",
        "007000",
        "007777"
    ])

    g = "\n".join([
        "000000",
        "000000",
        "000000",
        "000010",
        "000109",
        "001010"
    ])

    assert path_finder(a) == 0
    assert path_finder(b) == 2
    assert path_finder(c) == 4
    assert path_finder(d) == 42
    assert path_finder(e) == 14
    assert path_finder(f) == 0
    assert path_finder(g) == 4
