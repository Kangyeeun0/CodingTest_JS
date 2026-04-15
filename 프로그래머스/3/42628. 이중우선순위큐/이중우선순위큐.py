import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(heap, num)
        elif cmd == 'D' and heap:
            if num == 1:  # 최댓값 삭제
                heap.remove(max(heap))
                heapq.heapify(heap)
            else:  # 최솟값 삭제
                heapq.heappop(heap)
    
    if not heap:
        return [0, 0]
    
    return [max(heap), min(heap)]