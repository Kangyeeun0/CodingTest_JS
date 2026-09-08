import heapq
from collections import deque

def solution(jobs):
    answer = 0
    waiting_q = []
    heapq.heapify(waiting_q)
    current_time = 0
    n = len(jobs)
    
    for i in range(len(jobs)) :
        jobs[i] = [jobs[i][0], jobs[i][1], i]
    jobs.sort(key = lambda x:x[0])    
    jobs = deque(jobs)
    
    total_time = 0
        
    
    while waiting_q or jobs :
        # 현재시간이 맨 앞에 있는 job의 요청 시간보다 크면 대기열에 해당 job 넣기
        while jobs and current_time >= jobs[0][0] :
            job = jobs.popleft()
            heapq.heappush(waiting_q, [job[1], job[0], job[2]])
        
        # 대기열에 작업 존재하면 처리
        if waiting_q :
            job = heapq.heappop(waiting_q)
            # print(job)
            current_time += job[0]
            total_time += (current_time - job[1])
        else :
            if jobs :
                current_time = jobs[0][0]
                
    # print(current_time)
    # print(total_time)
    
    answer = total_time//n
    
    return answer