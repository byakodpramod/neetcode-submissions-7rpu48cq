class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(1,amount+1):
                dp[a] += dp[a-coin] if coin<=a else 0
        return dp[-1]