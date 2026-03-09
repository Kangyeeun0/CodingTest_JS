# 투 포인터 # 다시 풀어보기
def solution(sequence, k):
    left = 0
    answer=[0, len(sequence)]
    total = 0
    
    for right in range(len(sequence)) :
        total += sequence[right]
        
        while total > k :
            total -=sequence[left]
            left+=1
        
        if total == k :
            if right - left < answer[1] - answer[0] :
                answer=[left,right]
    
    return answer