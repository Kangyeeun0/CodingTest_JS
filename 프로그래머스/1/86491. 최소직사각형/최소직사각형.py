def solution(sizes):
    answer = 0
    max_a = 0
    max_b = 0
    
    for i in range(len(sizes)) :
        a,b = sizes[i]
        max_a = max(max(a,b), max_a)
        max_b = max(min(a,b), max_b)
    
        
    return max_a*max_b