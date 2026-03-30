class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i, slate):
            if i == len(nums):
                result.append(slate[:])
                return
            for idx in range(i, len(nums)):
                nums[idx],nums[i] = nums[i], nums[idx]
                slate.append(nums[i])
                helper(i+1, slate)
                nums[idx],nums[i] = nums[i], nums[idx]
                slate.pop()
        result = []
        helper(0, [])
        return result