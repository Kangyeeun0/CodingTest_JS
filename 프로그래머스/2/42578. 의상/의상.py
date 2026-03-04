def solution(clothes):
    answer = 1
    dict = {}
    
    for i in range(len(clothes)) :
        dict[clothes[i][1]] = dict.get(clothes[i][1],0) + 1
    
    for item, cnt in dict.items() :
        answer *= (cnt+1)
        
        
    return answer - 1