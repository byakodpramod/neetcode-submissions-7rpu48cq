class Solution:
    def jump(self, nums: List[int]) -> int:
        def helper(idx, hop):
            if idx >= len(nums)-1:
                res[0] = min(res[0], hop)
                return
            for i in range(1, nums[idx]+1):
                helper(idx+i, hop+1)
        res = [float('inf')]
        helper(0,0)
        return res[0]