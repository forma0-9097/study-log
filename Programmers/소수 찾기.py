from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    perm_set = set()
    answer = []
    
    for i in range(1, len(numbers)+1):
        
        for perm in permutations(numbers, i):
            perm_set.add(int(''.join(perm)))

    answer = [s for s in perm_set]
    
    return sum([1 for n in answer if is_prime(n)])
