from collections import deque

def solution(s):
    answer = 0
    extended = s*2
    
    for i in range(len(s)) :
        q= deque()
        window = extended[i: len(s)+i]
        valid = True

        for j in range(len(s)) :
            if window[j] == '[' or window[j] == '{' or window[j] == '(' :
                q.append(window[j])
            else :
                if not q :
                    valid = False
                    break
                if window[j] == ']' and q[-1] == '[' :
                    q.pop()
                elif window[j] == '}' and q[-1] == '{' :
                    q.pop()
                elif window[j] == ')' and q[-1] == '(' :
                    q.pop()
                else :
                    valid = False
                    break
                    
        if len(q) == 0  and valid:
            answer+=1
            
        
    return answer 