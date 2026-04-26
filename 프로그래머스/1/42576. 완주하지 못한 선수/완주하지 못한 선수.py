def solution(participant, completion):
    answer = ''
    dic = dict()
    
    for p in participant :
        dic[p] = dic.get(p, 0) + 1
    
    for c in completion :
        dic[c]-=1
        
    for name, n in dic.items() :
        if n != 0 :
            answer = name
    
    return answer