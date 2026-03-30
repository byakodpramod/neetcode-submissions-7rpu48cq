class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, slate):
            if i == len(nums):
                res.append(slate[:])
                return
            slate.append(nums[i])
            helper(i+1, slate)
            slate.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, slate)

        res=[]
        nums.sort()
        helper(0, [])
        return res