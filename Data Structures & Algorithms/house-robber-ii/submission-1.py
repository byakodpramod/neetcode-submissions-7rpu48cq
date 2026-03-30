class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums:
                return 0
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            if len(nums) >= 2:
                dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))