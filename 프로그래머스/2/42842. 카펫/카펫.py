def solution(brown, yellow):
    answer = []
    a = 1
    b= 1
    width = brown + yellow
    for i in range(1, int(yellow**(1/2))+1) :
        if yellow % i == 0 :
            a = i+2
            b = yellow //i + 2
            
            if a*b == width :
                return [b,a]

        
    return [b,a]