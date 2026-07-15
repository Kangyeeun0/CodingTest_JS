def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    puddles = set(map(tuple, puddles))
    
    dp[0][0] = 1
    
    for i in range(n) :
        for j in range(m) :
            if i == 0 and j == 0 :
                continue
            if (j+1,i+1) in puddles :
                dp[i][j] = 0
            else :
                if 0<=i-1<n and 0<=j-1<m :
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif 0<=i-1<n :
                    dp[i][j] = dp[i-1][j]
                elif 0<=j-1<m :
                    dp[i][j] = dp[i][j-1]
                
    # print(dp)
    return dp[-1][-1] % 1000000007