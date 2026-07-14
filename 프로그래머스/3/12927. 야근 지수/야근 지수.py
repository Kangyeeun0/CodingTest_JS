import heapq
def solution(n, works):
    answer = 0
    heap = []
    for work in works :
        heap.append(-work)
    heapq.heapify(heap)

    for i in range(n) :
        if abs(heap[0]) <= 0 :
            break
        work = heapq.heappop(heap)

        work = abs(work) - 1 
        heapq.heappush(heap, -work)
        
        
    while heap :
        a= heapq.heappop(heap)
        answer+=a*a
    
    return answer