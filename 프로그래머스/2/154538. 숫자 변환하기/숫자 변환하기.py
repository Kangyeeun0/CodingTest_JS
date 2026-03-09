from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    
    visited = set()
    
    while queue :
        cur, cnt = queue.popleft()
        if cur == y :
            return cnt
        
        
        for next in (cur+n, cur*2, cur*3) :
            if next not in visited and next<=y :
                visited.add(next)
                queue.append((next, cnt+1))
    
    return -1