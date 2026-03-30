class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        curMin, res = prices[0], 0
        for i in range(1,len(prices)):
            curMin = min(curMin, prices[i])
            res = max(res, prices[i]-curMin)
        return res