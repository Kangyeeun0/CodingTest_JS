def solution(s):
    answer = []
    s = s[2:-2]  # 양 끝의 {{ }} 제거
    sets = s.split('},{')  # 각 집합 분리
    # print(sets)
    
    sets = [list(map(int,st.split(','))) for st in sets]
    sets.sort(key = len)
    # print(sets)
    
    for i in range(len(sets)) :
        for j in range(len(sets[i])) :
            if sets[i][j] not in answer :
                answer.append(sets[i][j])
        
        
    
    return answer