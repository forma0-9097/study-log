def solution(numbers, target):
    count = 0
    
    def dfs(idx, sum_):
        nonlocal count
        
        if idx == len(numbers) and sum_ == target:
            count += 1

        if idx < len(numbers):
            dfs(idx + 1, sum_ + numbers[idx])
            dfs(idx + 1, sum_ - numbers[idx])
    
    dfs(0, 0)
    
    return count

'''
순서를 바꾸지 않고
적절히 더하거나 빼기
타겟 넘버와 같을 때

타겟 넘버를 만드는 방법의 수 (경우의 수)
:
dfs 재귀함수
''' 
