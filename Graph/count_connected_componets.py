def count_components(n, edges):
    # Step 1: Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    # Step 2: DFS function
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    # Step 3: Count components
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            components += 1
    
    return components


# Example
n = 5
edges = [(0,1), (1,2), (3,4)]
print(count_components(n, edges))
