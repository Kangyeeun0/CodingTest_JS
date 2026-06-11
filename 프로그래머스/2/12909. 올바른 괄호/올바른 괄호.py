from collections import deque
def solution(s):
    answer = True
    q_s= deque(s)
    cnt=0
    
    first = q_s.popleft()
    if first !="(" :
        return False
    else :
        cnt +=1
    
    while q_s :
        next_item = q_s.popleft()
        
        if next_item == '(' :
            cnt+=1
        elif next_item == ')' :
            cnt-=1
        
        if cnt < 0 :
            return False
    
    return True if cnt == 0 else False