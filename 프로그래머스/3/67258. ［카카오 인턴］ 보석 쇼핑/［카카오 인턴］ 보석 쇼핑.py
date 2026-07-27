def solution(gems):
    count = len(set(gems))
    answer = [0, len(gems)-1]
    gem_dic = {}
    left = 0
    # right = len(gems) -1
    
    for right in range(len(gems)) :
        gem_dic[gems[right]] = gem_dic.get(gems[right], 0) + 1
        
        while len(gem_dic) == count :
            
            if right - left < answer[1] - answer[0] :
                answer = [left, right]
            
            # if gem_dic[gems[left]] > 1 :
            gem_dic[gems[left]] -= 1
              
            if gem_dic[gems[left]] == 0 :
                del gem_dic[gems[left]]
            
            left+=1
        
    return [answer[0]+1,answer[1]+1]