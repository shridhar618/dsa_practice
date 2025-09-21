def build_adj_list(n, edges):
    # Step 1: create empty adjacency list
    graph = {i: [] for i in range(n)}
    
    # Step 2: add edges (undirected graph)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # comment this line if directed graph
    
    return graph


# Example
n = 4
edges = [(0,1), (0,2), (1,2), (2,3)]
print(build_adj_list(n, edges))
