from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q = deque()
    speeds = deque(speeds)
    
    for i in range(len(progresses)) :
        q.append(math.ceil((100-progresses[i]) / speeds[i]))
    # print(q)
    
    while q :
        first = q.popleft()
        count = 1
        while q and first >= q[0] :
            q.popleft()
            count+=1
        
        answer.append(count)    
        
    # print(answer)
    
    
    return answer