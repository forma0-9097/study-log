# 같은 숫자는 싫어
def solution(arr):
    stack = []
    
    for n in arr:
        if stack and n == stack[-1]:
            continue
        stack.append(n)
    
    return stack
    
'''
0~9까지
연속적으로 나타나는 숫자는/ 하나만 남기고/ 전부 제거
순서 유지

자료구조 stack
'''


#기능 개발
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for p, s in zip(progresses, speeds):
        queue.append(math.ceil((100-p)/s))
    
    while queue:
        progress = queue.popleft()
        ct = 1
        while queue and progress >= queue[0]:
            queue.popleft()
            ct += 1
        answer.append(ct)
    
    return answer
        
        
        
    
    
    return answer

'''
진도가 100일 때 서비스 반영 가능

기능의 개발 속도가 모두 다르다
뒤에 기능이 앞의 기능보다 먼저 개발될 수 있음 / 이때 뒤의 기능은 앞에 기능이 배포될 때 함께 배포

progresses 순서대로의 작업의 진도
speeds 작업의 개발속도

return 각 배포마다 몇개의 기능이 배포되는지

제한:
    진도율이 95%/ 하루에 4% 씩 진행되면/ 2일이 걸림
    
입출력:
    93 30 55
    1  30  5
    7  3   9
    [2, 1]
'''

#올바른 괄호
def solution(s):
    stack = []
    
    for p in s:
        if p == '(':
            stack.append(p)
        elif stack:
            stack.pop()
        else:
            return False
    
    return not stack


# 프로세스
from collections import deque

def solution(priorities, location):
    
    queue = deque()
    
    for i, p in enumerate(priorities):
        queue.append([i, p])
    
    sorted_priorities = deque(sorted(priorities, reverse=True))
    
    ct = 0

    while queue:
        i, num  = queue.popleft()

        if num < sorted_priorities[0]:
            queue.append((i, num))
        else:
            sorted_priorities.popleft()
            ct += 1
            if i == location:
                return ct
    

    '''
    특정 프로세스가 몇번째로 실행되는지 알아보기
        : 특정 프로세스에 인덱스
    큐에서 프로세스 하나 꺼내서
        : popleft
    큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
        : sorted된 우선순위와 비교
    다시 큐에 넣기
    없다면 넘어가기
    '''

# 주식가격
def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append(i)

    for idx in stack:
        answer[idx] = len(prices) - idx - 1
    
    return answer
