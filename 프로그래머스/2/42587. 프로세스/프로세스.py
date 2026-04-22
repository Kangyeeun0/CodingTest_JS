from collections import deque
def solution(priorities, location):
    answer = 1
    q = deque()
    for i in range(len(priorities)) :
        q.append([i, priorities[i]])
    # print(q)
    priorities.sort(reverse=True)
    i=0
    while q :
        index, priority = q.popleft()
        if priority == priorities[i] :
            if index == location :
                return answer
            else :
                answer+=1
            i+=1
        else :
            q.append([index, priority])
            
            
        
        
    return answer