from collections import deque
#9시부터 n회 t분 간격으로 역에 도착, 셔틀에는 최대 m명 탑승
def solution(n, t, m, timetable):
    answer = ''
    bus = 9 * 60
    min_time = deque()
    
    def change_time(time) :
        hour = time // 60
        minute = time % 60
        total = ""
        if hour <10 :
            total+="0" + str(hour) + ":"
        else :
            total += str(hour)+ ":"
        if minute < 10 :
            total+= "0" + str(minute)
        else :
            total += str(minute)
            
        return total
        
    
    for time in timetable :
        hour, minute = time.split(":")
        min_time.append(int(hour) * 60 + int(minute))   
    min_time = deque(sorted(min_time))
    
    for i in range(n) :
        cnt = 0
        while min_time and min_time[0] <= bus and cnt < m :
            last = min_time.popleft()
            cnt +=1
        if i == n - 1 :
            if cnt < m :
                answer = bus
            else :
                answer = last - 1
        bus += t
                
            
                
            
    
    
        
    
    
    return change_time(answer)