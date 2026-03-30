class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, slate):
            if i == len(nums):
                result.append(slate[:])
                return
            #exclude
            helper(i+1, slate)
            #include
            slate.append(nums[i])
            helper(i+1, slate)
            slate.pop()
        result = []
        helper(0, [])
        return result