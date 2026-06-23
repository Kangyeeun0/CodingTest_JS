from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque()
    queue.append([y,0])
    
    while queue :
        value, cnt = queue.popleft()
        
        if value == x :
            return cnt
        
        if value % 3 == 0 and value/3 >= x :
            queue.append([value/3, cnt+1])
        if value % 2 == 0 and value/2 >=x:
            queue.append([value/2, cnt+1])
        if value - n >= x :
            queue.append([value-n, cnt+1])
    
    return -1