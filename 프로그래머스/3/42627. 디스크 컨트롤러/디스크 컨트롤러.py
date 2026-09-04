import heapq

def solution(jobs):
    answer = 0
    #요청할 작업 큐
    need_q = []
    wait_q = []
    current_time = 0
    
    heapq.heapify(wait_q)
    heapq.heapify(need_q)
    
    for i in range(len(jobs)) :
        heapq.heappush(need_q, (jobs[i][0], jobs[i][1], i+1))
        
    # print(need_q)
        
    while need_q or wait_q :
        
        while need_q and current_time >= need_q[0][0] :
            start_time, need_time, num = heapq.heappop(need_q)
            heapq.heappush(wait_q, (need_time, start_time, num))
            
        if wait_q :
            need_time, start_time, num = heapq.heappop(wait_q)
            current_time += need_time
            # print(current_time)
            # print(current_time - start_time)
            answer+=(current_time - start_time)
        
        else :
            start_time, need_time, num = heapq.heappop(need_q)
            heapq.heappush(wait_q, (need_time, start_time, num))
            current_time = start_time
            
            
            
            
            
        
    
    
    
    
    return answer//len(jobs)