def solution(schedules, timelogs, startday):
    answer = 0
    # 시간 계산 함수
    def getTime(time) :
        h= time // 100
        m = time % 100
        m +=10
        if m>=60:
            h += m//60
            m = m%60
        return h*100+m
        
    
    for i in range(len(schedules)) :
        schedule = getTime(schedules[i])
        day = startday
        isRight = True
        for time in timelogs[i] :
            if 1<=(day%7)<=5 :
                if time > schedule :
                    isRight = False
                    # print(time)
                    break
            day+=1
            
        if isRight :
            # print(i)
            answer+=1
                    
            
    return answer