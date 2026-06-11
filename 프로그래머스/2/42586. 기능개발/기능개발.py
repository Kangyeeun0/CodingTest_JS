import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    rest = deque()
    
    for i in range(len(progresses)) :
        res_day = math.ceil((100-progresses[i])/speeds[i])
        rest.append(res_day)
    # print(rest)
    
    cnt = 0
    while rest :
        first = rest.popleft()
        cnt +=1
        while rest and first>=rest[0] :
            rest.popleft()
            cnt+=1

        answer.append(cnt)
        cnt=0
        
    return answer