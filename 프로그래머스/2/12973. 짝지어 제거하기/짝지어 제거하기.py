def solution(s):
    answer = -1
    stack = []
    
    for ch in s :
        if stack and ch == stack[-1] :
            stack.pop()
        else :
            stack.append(ch)
    
    if stack :
        return 0
    else :
        return 1
    
    return answer