def solution(clothes):
    answer = 1
    n = len(clothes)
    dic = {}
    
    for i in range(n) :
        dic[clothes[i][1]] = dic.get(clothes[i][1], 0) + 1
    
    arr = list(dic.values())
    for j in range(len(arr)) :
        answer*=(arr[j]+1)
    
    return answer - 1