# 部分和問題（DP）
def subset_sum(num_list: list[int], S: int) -> bool:
    N = len(num_list)
    dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num_list[i - 1]:
                dp[i][j] |= dp[i - 1][j - num_list[i - 1]]
    return dp[N][S]


# 最長共通部分文字列
def lcs(T: str, S: str) -> int:
    dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i == 0 or j == 0:
                continue
            if S[i - 1] == T[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
