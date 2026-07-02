def solution(s):
    answer = 0
    first_cnt = 0
    cnt = 0
    
    if len(s) == 1:
        return 1
    
    for i in range(0, len(s)) :
        if first_cnt == 0 and cnt == 0 :
            first_text = s[i]
            first_cnt +=1
        else :
            text = s[i]

            if first_text == text :
                first_cnt+=1
            else :
                cnt +=1

            if first_cnt == cnt :
                answer+=1
                cnt = 0
                first_cnt = 0
            
    if first_cnt != 0 :
        answer+=1
    
    
    return answer