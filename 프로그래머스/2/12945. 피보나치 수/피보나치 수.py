def solution(n):
    answer = 0
    stack = [0, 1]
    
    for i in range(2, n+1) :
        stack.append(stack[i-1] + stack[i-2])
        
    return stack[-1] % 1234567