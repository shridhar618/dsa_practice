from collections import deque

def path_exists(n, edges, src, dst):
    # Step 1: Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    
    # Step 2: BFS
    visited = set()
    queue = deque([src])
    
    while queue:
        node = queue.popleft()
        if node == dst:
            return True  # Found path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return False  # No path found


# Example
n = 5
edges = [(0,1), (1,2), (2,3)]
src, dst = 0, 3
print(path_exists(n, edges, src, dst))
