from collections import deque

def bfs(graph, start):
    visited = set()         # To track visited nodes
    queue = deque([start])  # Start BFS with given node
    
    while queue:
        node = queue.popleft()   # Take node from queue
        if node not in visited:
            print(node, end=" ") # Visit node
            visited.add(node)    # Mark visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add neighbors to queue


# Example
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
bfs(graph, 0)
