def solution(k, tangerine):
    answer = 0
    d= {} # 딕셔너리 생성
    
    for t in tangerine :
        d[t] = d.get(t, 0) + 1
    
    sorted_d = sorted(d.items(), key= lambda x: x[1], reverse = True)
    i=0
    total=0
    while total < k :
        total+=sorted_d[i][1]
        i+=1
        answer+=1
    return answer