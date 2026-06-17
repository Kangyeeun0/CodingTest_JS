def solution(sizes):
    answer = 0
    a = 0
    b = 0
    
    for i in range(len(sizes)) :
        sizes[i].sort()
    
    for j in range(len(sizes)) :
        if sizes[j][0] > a :
            a = sizes[j][0]
        if sizes[j][1] > b :
            b = sizes[j][1]
        
    
    return a*b