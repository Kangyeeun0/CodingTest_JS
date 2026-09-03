import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    rest_arr = deque([])
    for i in range(len(progresses)) :
        rest = 100 - progresses[i]
        rest_day = math.ceil(rest / speeds[i])
        rest_arr.append(rest_day)
        
    while rest_arr :
        task = rest_arr.popleft()
        sum_task = 1
        
        while rest_arr and task >= rest_arr[0] :
            rest_arr.popleft()
            sum_task +=1
            
        answer.append(sum_task)
        
    return answer