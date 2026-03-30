class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i,cur_sum, slate):
            if cur_sum == target:
                res.append(slate[:])
                return
            if i >= len(nums) or cur_sum > target:
                return
            helper(i+1, cur_sum, slate)
            slate.append(nums[i])
            helper(i, cur_sum+nums[i], slate)
            slate.pop()
        res = []
        helper(0, 0, [])
        return res