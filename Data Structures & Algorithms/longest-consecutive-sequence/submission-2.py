class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums, res = set(nums), 0
        for n in nums:
            tempRes, tempN = 1, n
            while tempN+1 in nums:
                tempRes += 1
                tempN += 1
            res = max(res, tempRes)
        return res