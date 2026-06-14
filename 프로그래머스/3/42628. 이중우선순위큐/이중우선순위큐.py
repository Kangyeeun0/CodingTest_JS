import heapq
def solution(operations):
    answer = []
    max_q = []
    min_q = []
    
    for i in range(len(operations)) :
        op, num = operations[i].split(" ")
        if op == 'I' :
            heapq.heappush(max_q, -int(num))
            heapq.heappush(min_q, int(num))
        elif op == 'D' :
            if num == '1' :
                if max_q and min_q:
                    heapq.heappop(max_q)
                    min_q.pop()
            elif num == '-1' :
                if max_q and min_q :
                    heapq.heappop(min_q)
                    max_q.pop()
    
    # print(max_q, min_q)
    if not max_q and not min_q :
        answer = [0,0]
    else :
        answer = [-max_q[0], min_q[0]]
    
    
    
    
    return answer