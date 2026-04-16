def solution(msg):
    answer = []
    list = [chr(i) for i in range(65, 91)]  # ['A', 'B', ..., 'Z']
    idx = 0
    
    while idx < len(msg):
        i = 1
        while idx + i <= len(msg) and msg[idx:idx+i] in list:
            i += 1
        
        w = msg[idx:idx+i-1]
        answer.append(list.index(w) + 1)
        
        if idx + i - 1 < len(msg):
            list.append(msg[idx:idx+i])
        
        idx += i - 1
    
    return answer