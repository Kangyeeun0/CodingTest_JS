from collections import deque
def solution(priorities, location):
    # answer = 0
    task = deque()
    sort_priority = sorted(priorities,reverse = True)
    
    for i in range(len(priorities)) :
        task.append([i, priorities[i]])
    # print(sort_priority)
    cnt = 1
    i=0
    while task :
        first = task.popleft()
        # print(first)
        
        if sort_priority[i] == first[1] :
            i += 1
            if first[0] == location :
                return cnt
            else :
                cnt+=1
        else :
            task.append(first)
        
        
                
        
        
        
    return cnt