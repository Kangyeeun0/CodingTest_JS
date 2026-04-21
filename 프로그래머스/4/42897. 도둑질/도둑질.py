def solution(money):
    answer = 0
    n = len(money)
    
    #경우 1: 첫 번째 집을 포함
    dp1 = [0] * (n-1)
    dp1[0] = money[0]
    dp1[1] = max(dp1[0], money[1])
    
    #경우 2: 두 번째 집을 포함
    dp2 = [0] * (n-1)
    dp2[0] = money[1]
    dp2[1] = max(dp2[0], money[2])
    
    for i in range(3, n) :
        dp1[i-1] = max(dp1[i-2], dp1[i-3]+money[i-1])
        dp2[i-1] = max(dp2[i-2], dp2[i-3]+money[i])
        
    return max(dp1[-1], dp2[-1])