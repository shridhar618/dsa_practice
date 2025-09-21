def has_cycle(n, edges):
    # Step 1: Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    
    # Step 2: DFS function with parent tracking
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):  # explore deeper
                    return True
            elif neighbor != parent:
                return True   # found a back edge → cycle
        return False
    
    # Step 3: Check every component
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):   # -1 means no parent for first node
                return True
    return False


# Example
n = 3
edges = [(0,1), (1,2), (2,0)]
print(has_cycle(n, edges))
