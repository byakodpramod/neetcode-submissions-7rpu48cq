class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(i, slate):
            if i == len(nums):
                res.append(slate[:])
                return
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    nums[j], nums[i] = nums[i], nums[j]
                    slate.append(nums[i])
                    helper(i+1, slate)
                    slate.pop()
                    nums[j], nums[i] = nums[i], nums[j]
        res = []
        helper(0, [])
        return res