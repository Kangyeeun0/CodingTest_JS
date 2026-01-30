def solution(x):
    answer = True
    arr=list(str(x))
    sum = 0
    for i in arr :
        sum = sum + int(i)
            
    if(x%sum) :
        return False;
    else :
        return True
    
    return answer