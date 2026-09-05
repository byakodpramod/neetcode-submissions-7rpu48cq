class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correctIdx = nums[i] - 1
            if 0<= correctIdx<len(nums) and nums[i] != nums[correctIdx]:
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i+=1
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return n +1