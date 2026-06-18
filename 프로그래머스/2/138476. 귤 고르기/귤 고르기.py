def solution(k, tangerine):
    answer = 0
    dic = dict()
    
    for i in range(len(tangerine)) :
        dic[tangerine[i]] = dic.get(tangerine[i], 0) + 1
        
    sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse = True))
    
    
    for (key, item) in sorted_dic.items() :
        k-= item
        answer+=1
        
        if k <=0 :
            return answer
    
    return answer