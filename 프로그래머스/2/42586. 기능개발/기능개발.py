def solution(progresses, speeds):
    answer = []
    days=[]
    
    for i in range(len(progresses)) :
        day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        days.append(day)
        
    count=1
    current=days[0]
    
    for j in range(1, len(days)) :
        if current < days[j] :
            answer.append(count)
            count=1
            current=days[j]
        else :
            count+=1
    answer.append(count)
    
    return answer