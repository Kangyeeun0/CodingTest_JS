import heapq
def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    
    while B :
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        
        if a < b :
            answer+=1
        else :
            heapq.heappush(A, a)
        # print(A)
    return answer