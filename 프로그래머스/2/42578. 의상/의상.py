def solution(clothes):
    answer = 1
    dic = dict()
    
    for clothe in clothes :
        name, kind = clothe
        dic[kind] = dic.get(kind, 0) + 1
    
    for value in dic.values() :
        answer *= (value+1)
    return answer - 1