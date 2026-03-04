def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # dp[i] : i 계단까지 오르는 방법의 수
    dp = [0] * (n + 1)
    dp[0] = 1 
    dp[1] = 1  

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 1칸 전 + 2칸 전 경우 합

    return dp[n] %1234567

