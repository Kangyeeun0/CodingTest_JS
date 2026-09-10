def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    
    while left < right :
        mid = (left + right) // 2 
        people = 0
        for time in times :
            people = people + (mid//time)
            
        if people >= n : # 정해진 수보다 크다면 시간 더 줄일 수 있음
            right = mid
            answer = mid
        else :
            left = mid+1
            
    return answer