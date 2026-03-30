class Solution:
    def longestCommonSubsequence(self, small: str, big: str) -> int:
        dp = [[0 for j in range(len(big) + 1)]
                 for i in range(len(small) + 1)]
        for i in range(len(small) - 1, -1, -1):
            for j in range(len(big) - 1, -1, -1):
                if small[i] == big[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]