from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque([(0, 0, 1)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < n and 0 <= ny < m) and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
            
    return -1
    

'''
최단거리: 
    bfs : 인접 노드 모두 방문, 
    queue : deque
    돌아가면 안됨 : visited
    
동서남북 방향으로 한칸씩 이동 : 방향 배열

조건:
  maps에서 1일 때만 
  도착 못할 시 -1

queue = deque((0, 0, 1))
TypeError: cannot unpack non-iterable int object
'''
