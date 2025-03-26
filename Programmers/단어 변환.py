from collections import deque

def solution(begin, target, words):

    queue = deque()
    queue.append((begin, 0))
    
    if target not in words:
        return 0
    
    while queue:
        cur_word, ct = queue.popleft()
        if cur_word == target:
            return ct
        
        for word in words:
            dif_ct = 0
            for cw, w in zip(cur_word, word):
                if cw != w:
                    dif_ct += 1
            if dif_ct == 1:
                queue.append((word, ct+1))
                        
    return 0
