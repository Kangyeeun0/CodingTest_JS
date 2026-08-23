from collections import deque
def solution(plans):
    answer = []
    waiting_works = deque()
    
    def changeTime(text) :
        hour, minute = text.split(":")
        
        return int(hour)*60+int(minute)
    
    # 전처리
    for plan in plans :
        plan[1] = changeTime(plan[1])
        plan[2] = int(plan[2])
        
    plans.sort(key=lambda x:x[1])
    # print(plans)
    
    current_time = plans[0][1]
    for i in range(len(plans)):
        
        if i+1 < len(plans) :
            if current_time + plans[i][2] <= plans[i+1][1] :
                current_time += plans[i][2]
                answer.append(plans[i][0])
                possible_time = plans[i+1][1] - current_time
                
                while waiting_works and possible_time > 0 :
                    work = waiting_works.pop()
                    if work[2] <= possible_time :
                        current_time += work[2]
                        answer.append(work[0])
                        possible_time -= work[2]
                    else :
                        remain = work[2] - possible_time
                        current_time+=possible_time
                        work[2] = remain
                        waiting_works.append(work)
                        possible_time = 0
                        
                # 밀린 과제까지 다 했는데도 시간이 남으면
                # 현재 시간 다음 과제 시작 시간으로 설정
                current_time = plans[i+1][1]
                
            else :
                possible_time = plans[i+1][1] - current_time
                current_time += possible_time
                remain_time = plans[i][2] - possible_time
                plans[i][2] = remain_time
                waiting_works.append(plans[i])
                
        else :
            answer.append(plans[i][0])
            current_time += plans[i][2]
            
            
    while waiting_works :
        work = waiting_works.pop()
        answer.append(work[0])
            
        
        
    
    return answer