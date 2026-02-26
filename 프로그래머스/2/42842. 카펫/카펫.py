def solution(brown, yellow):
    answer = []
    total = brown + yellow
    i=1
    a=0
    b=0
    while i*i <=total :
        if total % i == 0 :
            a = total //i
            b= i
        i+=1
        if (a-2) * (b-2) == yellow :
            return [a,b]
        
        
    return [a,b]