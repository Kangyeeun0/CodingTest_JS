def solution(data, ext, val_ext, sort_by):
    answer = []
    target = 0
    sort_target = 0
    
    if ext == 'code' :
        target = 0
    elif ext == 'date' :
        target = 1
    elif ext == 'maximum' :
        target = 2
    else :
        target = 3
    
    if sort_by == 'code' :
        sort_target = 0
    elif sort_by == 'date' :
        sort_target = 1
    elif sort_by == 'maximum' :
        sort_target = 2
    else :
        sort_target = 3
        
    
    for i in range(len(data)) :
        if data[i][target] < val_ext :
            answer.append(data[i])
    # print(answer)
    answer.sort(key=lambda x:x[sort_target])
            
        
    return answer