def solution(n):
    ans = 0
    start = n
    
    while start > 0 :
        if start % 2 == 0 :
            start= start/2
        else :
            start -= 1
            ans+=1
    
    

    return ans