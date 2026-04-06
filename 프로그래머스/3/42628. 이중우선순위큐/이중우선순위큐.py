from collections import deque 
def solution(operations):
    answer = []
    q=deque()
    
    for i in range(len(operations)) :
        text, number = operations[i].split(" ")
        if text == 'I' :
            q.append(int(number))
            q= deque(sorted(q))
        elif text == 'D' and number == '1':
            if q:
                q.pop()
        elif text == 'D' and number =='-1' :
            if q:
                q.popleft()
            
    arr=list(q)
    
    if not arr :
        return [0,0]
    elif len(arr) > 2 :
        return [arr[-1], arr[0]]
    elif len(arr) == 1 :
        return [arr[0], arr[0]]
    else :
        return arr[::-1]
    return answer