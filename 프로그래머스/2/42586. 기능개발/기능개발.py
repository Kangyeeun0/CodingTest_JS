import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    n = len(speeds)
    
    for i in range(n) :
        remain_day = math.ceil((100-progresses[i])/speeds[i])
        q.append(remain_day) 
        
    while q :
        day = q.popleft()
        total_day = 1
        i=0
        while q and day >=q[i] :
            q.popleft()
            total_day+=1
        answer.append(total_day)
        
    return answer