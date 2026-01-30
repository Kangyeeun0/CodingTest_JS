def solution(n):
    answer = 0
    i=1
    while True :
        if(n%i==1) :
            return i
        else :
           i = i+1
    
    return 