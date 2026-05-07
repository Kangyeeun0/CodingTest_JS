# from collections import defaultdict
def solution(keymap, targets):
    answer = []
    dic = dict()
    
    for i in range(len(keymap)) :
        key = keymap[i]

        for j in range(0, len(key)) :
            if key[j] in dic :
                dic[key[j]] = min(dic[key[j]], j+1)
            else :
                dic[key[j]] = j+1
                
    for i in range(len(targets)) :
        target = targets[i]
        cnt = 0
        for j in range(len(target)) :
            if not target[j] in dic : 
                cnt = -1
                break
            else :
                cnt +=dic[target[j]]
        answer.append(cnt)
                
    return answer