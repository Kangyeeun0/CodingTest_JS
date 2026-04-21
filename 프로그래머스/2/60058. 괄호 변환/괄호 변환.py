def solution(p):
    answer = ''
    #1. p가 빈문자열이면 빈문자열 리턴
    if not p :
        return ""
    
    #2. 올바른 괄호 문자열인지 확인
    def isCollectString(string) :
        total = 0
        for i in range(len(string)) :
            if total <1 and string[i] == ')' :
                return False
            elif string[i] == '(' :
                total+=1
            elif string [i] == ')' :
                total-=1
        if total == 0 :
            return True
        else :
             return False
            
    def separate(p) :
        count = 0
        for i in range(len(p)) :
            if p[i] == '(' :
                count += 1
            else :
                count -= 1
                
            if count == 0:
                return p[:i+1], p[i+1:]
        return p, ""
    
    u,v = separate(p)
    
    if isCollectString(u) :
        return u + solution(v)
    
    else :
        temp = '('  + solution(v) + ')'
        
        u = u[1:-1]
        u = ''.join('(' if char == ")" else ")" for char in u)
        
        return temp+u
    
    
    
    return answer