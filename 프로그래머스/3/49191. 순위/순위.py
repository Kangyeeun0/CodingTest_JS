def solution(n, results):
    
    win = [[False] * (n+1) for _ in range(n+1)]
    
    #직접 경기 결과 입력
    for a,b in results :
        win[a][b] = True
        
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                #i가 k를 이기고, k가 j를 이기면
                #i는 j를 이김
                if win[i][k] and win[k][j] :
                    win [i][j] = True
                    
    answer = 0
    
    for i in range(1, n+1) :
        known = 0 # i번 선수와 승패가 명확한 선수 수
        
        for j in range(1, n+1) :
            if i != j:
                #i가 j를 이기거나, j가 i를 이기면
                if win[i][j] or win[j][i] :
                    known += 1
        
        if known == n-1 :
            answer += 1
    
    return answer