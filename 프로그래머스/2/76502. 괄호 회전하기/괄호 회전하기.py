def solution(s):
    answer = 0
    n = len(s)
    s= s*2
    # print(s)
    
    for i in range(n) :
        stack = []
        for j in range(i, i+n):
            if s[j] in ['(', '{', '['] :
                stack.append(s[j])
            elif s[j] == ')' :
                if stack and stack[-1] == '(' :
                    stack.pop()
                else :
                    stack.append(s[j])
            elif s[j] == '}' :
                if stack and stack[-1] == '{' :
                    stack.pop()
                else :
                    stack.append(s[j])
            elif s[j] == ']' :
                if stack and stack[-1] == '[' :
                    stack.pop()
                else :
                    stack.append(s[j])
      
        if not stack :
            answer+=1

    
    
    return answer