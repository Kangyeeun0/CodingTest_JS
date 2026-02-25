def solution(n):
    answer = 0
    nextNum=n+1
    a=bin(n)[2:]
    while True :
        b=bin(nextNum)[2:]
        
        if(a.count('1') == b.count('1')) :
            return nextNum
        else :
            nextNum+=1
        
    return answer