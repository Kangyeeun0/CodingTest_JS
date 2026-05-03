from collections import deque
def solution(priorities, location):
    answer = 1
    waiting_q = deque()
    sort_priorities = sorted(priorities, reverse = True)
    
    for i in range(len(priorities)) :
        waiting_q.append([i,priorities[i]])
    # print(waiting_q)
    i=0
    
    while waiting_q :
        l, p = waiting_q.popleft()
        # print(l,p)
        
        if p == sort_priorities[i] :
            if l == location :
                return answer
            else :
                answer+=1
                i+=1
        else :
            waiting_q.append([l,p])
            
        
    return answer