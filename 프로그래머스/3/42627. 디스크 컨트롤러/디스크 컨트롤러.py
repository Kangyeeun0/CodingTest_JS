import heapq
from collections import deque

def solution(jobs):
    answer = []
    wait_q = []
    heapq.heapify(wait_q)
    not_start_jobs = []
    current_time = 0
    cnt = len(jobs)
    
    for i in range(len(jobs)) :
        start, need = jobs[i]
        not_start_jobs.append([need, start, i])
    
    not_start_jobs.sort(key=lambda x:(x[1], x[0], x[2]))
    not_start_jobs = deque(not_start_jobs)
    first = not_start_jobs.popleft()
    current_time = first[1]
    heapq.heappush(wait_q, first)

    
    while wait_q : 
        job = heapq.heappop(wait_q)
        current_time += job[0]
        answer.append(current_time - job[1])
        
        while not_start_jobs and current_time >= not_start_jobs[0][1] :
            next_job = not_start_jobs.popleft()
            heapq.heappush(wait_q, next_job)
        
        if not wait_q :
            if not_start_jobs:
                next_job = not_start_jobs.popleft()
                heapq.heappush(wait_q, next_job)
                current_time = next_job[1]

        
    
    return sum(answer)//cnt