class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * (amount)
        for a in range(1,amount+1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], 1+dp[a-c])
        return -1 if dp[amount] == float('inf') else dp[amount]