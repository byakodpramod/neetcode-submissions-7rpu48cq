class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        l,res, curSum=0,float("inf"),0
        for r in range(len(nums)):
            curSum += nums[r]
            while l<=r and curSum >= target:
                res = min(res, r-l+1)
                curSum -= nums[l]
                l += 1
        return res if res != float("inf") else 0