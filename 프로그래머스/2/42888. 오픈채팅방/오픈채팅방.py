from collections import deque
def solution(record):
    answer = []
    chat = deque()
    dic = {}
    
    for r in record :
        if r[0:5] == 'Leave' :
            text, id = r.split(" ")
        else :
            text, id, name= r.split(" ")
            
        if text == 'Change' :
            dic[id] = name
        elif text == "Enter":
            chat.append([text, id])
            dic[id] = name
        else :
            chat.append([text, id])
            
    # print(chat, dic)
    while chat :
        text, id = chat.popleft()
        if text == 'Enter' :
            answer.append(dic[id]+"님이 들어왔습니다.")
        elif text == 'Leave' :
            answer.append(dic[id]+"님이 나갔습니다.")
    
    
        
    
    return answer