import heapq
def solution(jobs):
    jobs.sort()
    
    current_time = 0
    total_time = 0
    heap=[]
    job_idx = 0
    completed = 0
          
    
    while completed < len(jobs) :
        while job_idx < len(jobs) and jobs[job_idx][0] <= current_time :
            heapq.heappush(heap, (jobs[job_idx][1], jobs[job_idx][0])) #(소요시간, 요청시간)
            job_idx+=1
            
        if heap :
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            total_time +=current_time - request_time
            completed+=1
        else :
            current_time = jobs[job_idx][0]
    return total_time // len(jobs)
        
    print(arr)
    return answer