def solution(s):
    answer = True
    cnt = 0
    
    if s[0] == ')' :
        return False
    
    for k in s :
        if k == '(' :
            cnt+=1
        else :
            cnt-=1
        
        if cnt <0 :
            return False
        
    if cnt !=0 :
        return False
        
        

    return True