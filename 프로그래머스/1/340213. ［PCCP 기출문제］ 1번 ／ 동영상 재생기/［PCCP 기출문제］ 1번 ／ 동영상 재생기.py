def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def change_min(time) :
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
    
    current_time = change_min(pos)
    
    for command in commands :
        
        if change_min(op_start)<=current_time<change_min(op_end) :
            current_time = change_min(op_end)
        
        if command == 'next' :
            if current_time + 10 <= change_min(video_len) :
                current_time += 10
            else :
                current_time = change_min(video_len)
        elif command == 'prev' :
            if current_time - 10 >= 0 :
                current_time -= 10
            else :
                current_time = 0
        # print(current_time)
    if change_min(op_start)<=current_time<change_min(op_end) :
        current_time = change_min(op_end)
    
    # print(current_time)        
    current_hour = current_time//60
    current_minute = current_time % 60
    
    if current_hour < 10 :
        answer += "0"+str(current_hour)
    else :
        answer+= str(current_hour)
        
    if current_minute < 10 :
        answer+= ":" + "0"+ str(current_minute)
    else :
        answer+= ":" + str(current_minute)
    
    return answer