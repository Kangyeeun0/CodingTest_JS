import heapq
def solution(n, k, enemy):
    answer = 0
    max_heap = []
    i = 0
    
    if k >=len(enemy) :
        return len(enemy)
    
    while i<len(enemy) :
        if n >= enemy[i] :
            n-=enemy[i]
            heapq.heappush(max_heap,-enemy[i])
            answer+=1
            i+=1
        elif n < enemy[i] and k > 0 :
            heapq.heappush(max_heap,-enemy[i])
            n-=enemy[i]
            if max_heap :
                max_value = -heapq.heappop(max_heap)
                n+=max_value
                k-=1
                answer+=1
                i+=1
            else :
                k-=1
                i+=1
                answer+=1
            
        else :
            break
    return answer