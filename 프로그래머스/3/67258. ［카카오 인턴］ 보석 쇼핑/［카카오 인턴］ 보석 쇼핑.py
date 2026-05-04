def solution(gems):
    answer = []
    gems_dict = {}
    min_len = len(gems) + 1
    left = 0
    gem_cnt = len(set(gems))
    
    for i in range(len(gems)) :
        right = i
        gem = gems[i]
        gems_dict[gem] = gems_dict.get(gem, 0) + 1
        
        while gem_cnt == len(gems_dict) :
            if min_len > right - left + 1 :
                min_len = right - left + 1
                answer = [left+1, right+1]
                
            gems_dict[gems[left]] -= 1
            
            if gems_dict[gems[left]] == 0 :
                del gems_dict[gems[left]]
            left+=1
        
    return answer