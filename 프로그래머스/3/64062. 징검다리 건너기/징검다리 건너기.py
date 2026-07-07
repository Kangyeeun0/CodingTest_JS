def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    print(left, right)
    
    while left <= right :
        mid = (left+right) // 2
        cnt = 0
        can_cross = True
        
        for stone in stones :
            if stone < mid :
                cnt +=1
            else :
                cnt = 0

                
            if cnt >= k :
                can_cross = False
                break
                
        if can_cross :
            answer = mid
            left = mid + 1
        else :
            right = mid - 1
            
            
        
                
                
    return answer