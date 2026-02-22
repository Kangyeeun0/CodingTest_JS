def solution(n, m):
    a=n
    b=m
    
    while b!=0 :
        temp = b
        b= a%b
        a=temp
    
    maxV=int(n*m / a)
    print(maxV)
    return [a,maxV]