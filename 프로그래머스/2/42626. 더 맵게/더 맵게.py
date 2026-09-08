import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 :
        first = heapq.heappop(scoville)
        if first >= K :
            return answer
        second = heapq.heappop(scoville)
        mix = first + (second*2)
        heapq.heappush(scoville, mix)
        answer+=1
        
    if scoville and scoville[0] >= K :
        return answer
    else :
        return -1
    
    return answer