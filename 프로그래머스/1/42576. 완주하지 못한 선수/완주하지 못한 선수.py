def solution(participant, completion):
    answer = ''
    dic = dict()
    
    for p in participant :
        dic[p] = dic.get(p, 0) + 1
    
    for c in completion :
        if c in dic :
            dic[c] -= 1
        if dic[c] == 0 :
            del dic[c]
    
    for key in dic :
        answer=key
        
    return answer