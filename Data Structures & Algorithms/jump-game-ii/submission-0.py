class Solution:
    def jump(self, nums: List[int]) -> int:
        def helper(idx, hops):
            # print(idx,hops)
            if idx >= len(nums)-1:
                res[0] = min(res[0],hops)
                return
            for j in range(1,nums[idx]+1):
                helper(idx+j, hops+1)
        res = [float("inf")]
        helper(0,0)
        return res[0]