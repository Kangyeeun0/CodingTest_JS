from collections import deque
def solution(A, B):
    answer = 0
    a_q = deque(sorted(A, reverse=True))
    b_q = deque(sorted(B, reverse=True))
    
    if a_q[-1] >= b_q[0] :
        return 0
    
    while a_q :
        if a_q and b_q :
            if a_q[0] <b_q[0] :
                a_q.popleft()
                b_q.popleft()
                answer+=1
            else :
                a_q.popleft()
        
    
    
    
    
    
    
    
    return answer