def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    
    for i in range(len(skill_trees)) :
        target = skill_trees[i]
        k = 0
        cnt = 0
        for j in range(len(target)) :
            if target[j] in skill :
                if target[j] == skill[k] :
                    k +=1
                cnt+=1
        if k == cnt :
            answer+=1
                    
                
                
        
    return answer