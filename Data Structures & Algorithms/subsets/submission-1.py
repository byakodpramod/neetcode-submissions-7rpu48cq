class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        slate = []
        def dfs(i):
            if i >= len(nums):
                res.append(slate[:])
                return
            slate.append(nums[i])
            dfs(i+1)
            slate.pop()
            dfs(i+1)
        dfs(0)
        return res