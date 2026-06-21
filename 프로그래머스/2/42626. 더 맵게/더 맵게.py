import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    for i in range(len(scoville) - 1) :
        if scoville[0] >= K :
            return answer
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            mix = first + second * 2
            heapq.heappush(scoville, mix)
            answer+=1
        
    if scoville[0] < K :
        return -1
    return answer