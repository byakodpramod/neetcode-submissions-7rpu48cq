class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        res = 0
        for n in nums:
            count = 0
            if n-1 not in numSet:
                count += 1
                while n+1 in numSet:
                    count += 1
                    n += 1
                res = max(res, count)
        return res
