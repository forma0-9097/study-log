def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    
    return ''.join(sorted_numbers) if sorted_numbers[0] != '0' else '0'

'''
map()
list()
sorted()
lambda 익명함수
join()
'''
