def solution(n, stations, w):
    answer = 0
    current = 1
    idx = 0
    
    while current <= n :
        if idx < len(stations) and current >= stations[idx]-w :
            current = stations[idx] + w + 1
            idx+=1
        else :
            answer+=1
            current += w*2 + 1
        
    

    

    return answer