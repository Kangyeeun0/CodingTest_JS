def solution(n, times):
    answer = 0
    # 이분탐색 범위 설정
    left = 1
    right = max(times) * n # 최악의 경우 : 가장 느린 심사대에서 모두 처리
    
    answer = right
    
    while left <= right :
        mid = (left+right) // 2
        
        #mid 시간 동안 심사 가능한 총 인원 계산
        total = 0
        for time in times :
            total += mid // time
            
        if total >= n : #mid 시간 안에 n명 이상 심사 가능
            answer = mid
            right = mid -1
        else :
            left = mid + 1
       
    return answer