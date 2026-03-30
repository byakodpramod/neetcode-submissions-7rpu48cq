class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fprod = 1
        output = [1] * len(nums)
        for i in range(len(output)):
            output[i] *= fprod
            fprod *= nums[i]
        bprod = 1
        for j in reversed(range(len(nums))):
            output[j] *= bprod
            bprod *= nums[j]
        return output