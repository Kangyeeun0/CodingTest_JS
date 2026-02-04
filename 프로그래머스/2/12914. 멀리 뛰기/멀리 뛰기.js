function solution(n) {
    const MOD = 1234567;
    const dp = Array(n + 1).fill(0);

    dp[0] = 1; // 0을 만드는 경우 1가지 (아무것도 선택하지 않음)
    dp[1] = 1; // 1을 만드는 경우 1가지 (1)

    for (let i = 2; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    return dp[n];
}
