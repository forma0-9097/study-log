from collections import deque

def solution(n, computers):
    
    queue = deque()
    visited = [False] * n
    
    for i, computer in enumerate(computers):
        if not visited[i]:
            queue.append(computer)
            visited[i] = True

            while queue:
                q_com = queue.popleft()
                for j, value in enumerate(q_com):
                    if not visited[j] and value == 1:
                        visited[j] = True
                        queue.append(computers[j])
                        n -= 1
                        
    return n

'''
네트워크 :
    bfs
queue :
    자기 자신을 제외한 위치의 값이 1일 때
    
visited

for:
    computers 모두 돌아가면서
    queue에 넣어준다
    visited
    
while queue:
    for문 in popleft
        조건 not visited[i]
        visited
        queue.append
        연결될 때마다 n - 1씩 해주면 됨

'''

from collections import deque

def solution(n, computers):
    
    queue = deque()
    visited = [False] * n

    network_count = 0

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            queue.append(i)

            while queue:
                node = queue.popleft()
                for j in range(n):
                    if not visited[j] and computers[node][j] == 1:
                        visited[j] = True
                        queue.append(j)

            network_count += 1

    return network_count
