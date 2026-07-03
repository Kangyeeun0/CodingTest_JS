def solution(X, Y):
    answer = ''
    cntX = [0] * 10
    cntY = [0] * 10
    
    for x in X :
        cntX[int(x)] += 1
    for y in Y :
        cntY[int(y)] += 1
        
    for i in range(9, -1, -1) :
        answer += str(i) * min(cntX[i], cntY[i])
        

    if answer == "" :
        return "-1"
    if answer[0] == '0' :
        return "0"
    return answer