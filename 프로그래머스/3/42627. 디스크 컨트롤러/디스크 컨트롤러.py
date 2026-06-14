import heapq
def solution(jobs):
    answer = 0
    wait_q = []
    heapq.heapify(wait_q)
    heapq.heapify(jobs)
    current_time = 0
    i=0
    total_time = []
    
    while jobs or wait_q :
        while jobs and jobs[0][0] <= current_time :
                job = heapq.heappop(jobs)
                heapq.heappush(wait_q, [job[1], job[0]])
                
        if wait_q :
            current_job = heapq.heappop(wait_q)
            # print(current_job)
            current_time += current_job[0]
            # print(current_time)
            total_time.append(current_time - current_job[1])
        else :
            current_time = jobs[0][0]
            
            
    for i in range(len(total_time)) :
        answer+=total_time[i]
                

    return answer // len(total_time)