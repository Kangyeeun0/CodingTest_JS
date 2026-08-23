# 미사일을 최소로 사용
# dp 문제
def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])
    # print(targets)
    current_dot = targets[0][1]
    
    for target in targets :
        
        if current_dot <= target[0] :
            current_dot = target[1]
            answer+=1
            # print(current_dot)
        
        
    
    return answer