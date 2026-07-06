#아이디 길이: 3~ 15
# -. _, ., 숫자 무소문자 가능
# 마침표는 처음과 끝 사용 금지, 연속 사용 금지
def solution(new_id):
    answer = ''
    comma_cnt= 0
    
    id=new_id.lower()
    # print(id)
    
    for i in range(len(id)) :
        if id[i] == '.' :
            if comma_cnt == 0 :
                comma_cnt +=1
                answer+=id[i]
            else :
                continue
        elif id[i].islower() or id[i].isdigit() or id[i] == '-' or id[i] == '_'  :
            if comma_cnt != 0 :
                comma_cnt = 0
            answer+=id[i]
        else :
            continue
            
 
    if answer[0] == '.' :
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[0:-1]
    if answer == "" :
        answer +='a'
            
    if len(answer) >=16 :
        answer = answer[0:15]
        if answer[-1] == '.' :
            answer =  answer[0: -1]
    elif len(answer) <=2 :
        # print(answer)
        if answer[-1] == '.' :
            answer = answer[0: -1]
        while len(answer) <3 :
            answer+=answer[-1]  
    


        
            
    return answer