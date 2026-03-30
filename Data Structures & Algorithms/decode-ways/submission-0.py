class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s) + [1]
        for i in reversed(range(len(s))):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i + 1]
                if i < len(s) - 1 and s[i : i + 2] <= '26':
                    dp[i] += dp[i + 2]
        return dp[0]