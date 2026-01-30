def solution(n):
    answer = 0
    
    sqrt=n**0.5
    
    if(sqrt==int(sqrt)) :
        return (sqrt+1)**2
    else :
        return -1
    return