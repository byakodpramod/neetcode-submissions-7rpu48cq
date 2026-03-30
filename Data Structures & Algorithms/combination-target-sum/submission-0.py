class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, cur_sum, slate):
            if cur_sum == target:
                result.append(slate[:])
                return
            for idx in range(i,len(nums)):
                if cur_sum+nums[idx] > target:
                    break
                slate.append(nums[idx])
                helper(idx, cur_sum+nums[idx], slate)
                slate.pop()
        nums.sort()
        result = []
        helper(0,0,[])
        return result