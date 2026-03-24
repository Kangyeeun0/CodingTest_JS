def solution(s):
    answer = -1
    stack = []
    length = len(s)
    
    for i in range(length) :
        if not stack :
            stack.append(s[i])
        elif stack[-1] == s[i] :
            stack.pop()
        else :
            stack.append(s[i])
    
    if stack :
        return 0
    else :
        return 1

    return answer