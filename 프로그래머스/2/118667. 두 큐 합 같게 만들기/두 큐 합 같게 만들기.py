from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1=deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1+sum2
    
    if total%2 :
        return -1
    
    target = total // 2
    i=0
    while i<=len(queue1)*3 :
        if sum1==target :
            return answer
        elif sum1 > target :
            if not q1 :
                return -1
            k=q1.popleft()
            q2.append(k)
            sum1-=k
            sum2+=k
            answer+=1
        elif sum1 < target :
            if not q2 :
                return -1
            k=q2.popleft()
            q1.append(k)
            sum1+=k
            sum2-=k
            answer+=1
        i+=1
            
    return -1