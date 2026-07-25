def solution(sequence, k):
    answer = []
    left = 0
    right = 0
    total = 0
    
    for right in range(len(sequence)) :
        total += sequence[right]
        
        while total > k :
            total-=sequence[left]
            left +=1
        
        if total == k :
            if not answer :
                answer = [left, right]
            else :
                if answer[1] - answer[0] > right - left :
                    answer = [left, right]
        
    return answer