import heapq
def solution(n, s):
    
    if n > s :
        return [-1]
    
    k = s // n
    r = s % n
    answer = [k for _ in range(n)]
    heapq.heapify(answer)
    # print(answer)
    
    while r > 0 :
        value = heapq.heappop(answer)
        heapq.heappush(answer, value+1)
        r-=1
        
    return sorted(answer)