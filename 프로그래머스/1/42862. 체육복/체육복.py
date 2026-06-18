def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    lost = lost_set - reserve_set
    reserve = reserve_set - lost_set
    
    answer = n - len(lost)
    
    
    for l in sorted(lost) :
        if l-1 in reserve :
            answer+=1
            reserve.remove(l-1)
        elif l+1 in reserve :
            answer+=1
            reserve.remove(l+1)
        else :
            continue
            
    return answer