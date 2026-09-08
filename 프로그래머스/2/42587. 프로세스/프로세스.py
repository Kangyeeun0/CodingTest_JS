from collections import deque
def solution(priorities, location):
    answer = 0
    tasks = deque([])
    order = sorted(priorities[:], reverse=True)
    
    for i in range(len(priorities)) :
        tasks.append([priorities[i],i])
        
    k = 0

    while tasks :
        task = tasks.popleft()
        # print(task)
        if task[0] == order[k] :
            answer+=1
            k+=1
            if task[1] == location :
                return answer
        else :
            tasks.append(task)
        
        
    
    
                      
    
    return answer