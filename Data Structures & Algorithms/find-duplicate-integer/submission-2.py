class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            indexRep = abs(nums[i])-1
            if nums[indexRep] < 0:
                return abs(nums[i])
            nums[indexRep] = -1 * nums[indexRep]
        return -1