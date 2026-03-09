def solution(skill, skill_trees):
    answer = 0
    arr = list(skill)
    
    answerArr=[]
    
    for i in range(len(skill_trees)) :
        n=0
        isSkill = True
        for ch in skill_trees[i] :
            if ch in skill and ch == skill[n] :
                n+=1
                isSkill = True
            elif ch in skill and ch!=skill[n] :
                n=0
                isSkill = False
                break
        
        if isSkill :
            answer+=1
            answerArr.append(skill_trees[i])
        print(answerArr)    
    return answer