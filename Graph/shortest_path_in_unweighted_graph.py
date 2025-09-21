from collections import deque

def shortest_path(n, edges, src):
    # Step 1: Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    
    # Step 2: Distance array, initialize with -1 (unreachable)
    dist = [-1] * n
    dist[src] = 0
    
    # Step 3: BFS
    queue = deque([src])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:   # not visited yet
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist


# Example
n = 4
edges = [(0,1), (0,2), (1,2), (2,3)]
src = 0
print(shortest_path(n, edges, src))
