import heapq
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x:x[0])
    completed = 0
    current_time = 0
    total_time = 0
    job_index = 0
    waiting_jobs = []
    # heapq.heapify(waiting_jobs)
    
    
    while completed < len(jobs) :
        while job_index < len(jobs) and jobs[job_index][0] <= current_time :
                heapq.heappush(waiting_jobs,(jobs[job_index][1],jobs[job_index]))
                job_index+=1
        
        if waiting_jobs :
            priority, job = heapq.heappop(waiting_jobs)
            current_time += job[1]
            total_time += current_time - job[0]
            completed+=1
        else :
            if job_index < len(jobs):
                current_time = jobs[job_index][0]
        
        
        
                
    return total_time //len(jobs)