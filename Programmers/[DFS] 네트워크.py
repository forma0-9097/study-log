def solution(n, computers):
    
    def dfs(node):
        visited[node] = True
        
        for idx, connected in enumerate(computers[node]):
            if not visited[idx] and connected == 1:
                dfs(idx)
    
    network_count = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1
    
    return network_count
