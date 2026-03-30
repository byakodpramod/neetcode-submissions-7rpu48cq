class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProd = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= forwardProd
            forwardProd *= nums[i]
        backwardProd = 1
        for j in reversed(range(len(nums))):
            output[j] *= backwardProd
            backwardProd *= nums[j]
        return output