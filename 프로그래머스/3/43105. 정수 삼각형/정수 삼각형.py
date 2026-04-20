def solution(triangle):
    answer = 0
    triangle = triangle[::-1]
    dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
    dp[0] = triangle[0]
    

    for i in range(1,len(triangle)) :
        for j in range(len(triangle[i])) :
            dp[i][j] = triangle[i][j]+max(dp[i-1][j], dp[i-1][j+1])
    
    
    return dp[-1][-1]