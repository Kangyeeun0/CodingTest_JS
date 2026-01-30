def solution(n):
    answer = 0
    
    for i in range(n) :
        if(n%(i+1)==0) :
            answer= answer + i+1
            
    return answer