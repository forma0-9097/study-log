from collections import deque

def on_line(x, y, rectangle): 
    on_rec = set()
    for i, (x1, y1, x2, y2) in enumerate(rectangle):
        if (x1 <= x <= x2 and y in (y1, y2)) or (y1 <= y <= y2 and x in (x1, x2)):
            on_rec.add(i)
    return on_rec

def in_rectangle(x, y, rectangle):
    for x1, y1, x2, y2 in rectangle:
        if x1 < x < x2 and y1 < y < y2:
            return True
    return False

def is_penetrate(cX, cY, nX, nY, rectangle):
    for x1, y1, x2, y2 in rectangle:
        if ((len(set([x1, x2]) & set([cX, nX])) == 2 and y1 < cY < y2) 
            or (len(set([y1, y2]) & set([cY, nY])) == 2 and x1 < cX < x2)):
            return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append((characterX, characterY))
    visited = {(characterX, characterY) : 0}
    
    while queue:
        cX, cY = queue.popleft()
        distance = visited[(cX, cY)]
        cur_on_rec = on_line(cX, cY, rectangle)
        
        for mX, mY in mv:
            nX, nY = cX + mX, cY + mY
            
            if (1 <= nX and 1 <= nY
                and (nX, nY) not in visited
                and len(cur_on_rec & on_line(nX, nY, rectangle)) > 0 
                and not in_rectangle(nX, nY, rectangle)
                and not is_penetrate(cX, cY, nX, nY, rectangle)):
                
                if nX == itemX and nY == itemY:
                    return distance + 1
                
                visited[(nX, nY)] = distance + 1
                queue.append((nX, nY))
    
    return visited[(itemX, itemY)]
            
