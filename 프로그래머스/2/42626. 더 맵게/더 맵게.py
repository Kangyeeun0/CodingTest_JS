import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K :
        return answer

    for i in range(len(scoville)-1) : 
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer+=1
        if scoville[0] >= K :
            return answer

    return -1