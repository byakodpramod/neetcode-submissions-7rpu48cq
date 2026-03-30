class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(i,slate):
            if i>=len(nums):
                res.append(slate[:])
                return
            helper(i+1, slate)
            slate.append(nums[i])
            helper(i+1, slate)
            slate.pop()
        helper(0,[])
        return res