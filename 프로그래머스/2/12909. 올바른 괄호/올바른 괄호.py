from collections import deque

def solution(s):
    answer = True
    q=deque()
    
    for k in s :
        if k == ')' and len(q)==0:
            answer=False
            break
        elif k == '(' :
            q.append(k)
        elif k == ')' and q[-1]=='(' :
            q.pop()
            
    if len(q)!=0 :
        answer=False
    return answer