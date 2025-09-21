def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()   # Keep track of visited nodes
    
    if node not in visited:
        print(node, end=" ")   # Visit the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Example
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
dfs(graph, 0)
