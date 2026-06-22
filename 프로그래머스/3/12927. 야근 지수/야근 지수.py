import heapq
def solution(n, works):
    answer = 0
    for i in range(len(works)) :
        works[i] = -works[i]
    heapq.heapify(works)
    
    for i in range(n) :
        work = -heapq.heappop(works)
        if work > 0 :
            work -= 1
            heapq.heappush(works, -work)
        else :
            break
            
    for i in range(len(works)) :
        answer += works[i] ** 2
    
        
    # print(works)
        
    
    
    
    return answer