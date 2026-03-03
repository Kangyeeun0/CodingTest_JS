def solution(k, tangerine):
    answer = 0
    d = {}
    
    for i in tangerine :
        d[i] = d.get(i, 0) + 1
    
    counts = sorted(d.values(), reverse=True)
    
    for j in range(len(counts)) :
        if k-counts[j] >0 :
            k-=counts[j]
            answer+=1
        else :
            answer+=1
            break
    
    
    return answer