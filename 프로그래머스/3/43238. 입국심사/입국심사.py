def solution(n, times):
    answer = 0
    right = n * max(times)
    left = 0
    
    while left < right :
        mid = (left+right) // 2
        people = 0
        for time in times :
            people+= mid//time
            
        if people >= n :
            right = mid
            answer = mid
        else :
            left = mid + 1
            
    
    
    
    return answer