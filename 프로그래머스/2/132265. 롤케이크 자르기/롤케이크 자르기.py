from collections import Counter
def solution(topping):
    answer = 0
    dic = dict()
    left = set()
    right = len(set(topping))
    
    for t in topping :
        dic[t] = dic.get(t, 0) + 1
    for i in range(len(topping)) :
        t = topping[i]
        left.add(t)
        dic[t] -= 1
        if dic[t] == 0 :
            right -= 1
        if len(left) == right :
            answer+=1

        
        
    return answer