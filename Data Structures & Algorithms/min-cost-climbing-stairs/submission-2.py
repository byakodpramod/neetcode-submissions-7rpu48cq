class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return o
        dp = [0 for _ in range(len(cost))]
        dp[0],dp[1] = cost[0],cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1],dp[-2])