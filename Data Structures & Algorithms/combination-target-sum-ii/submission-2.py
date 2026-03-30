class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, cur_sum, slate):
            if cur_sum == target:
                res.append(slate[:])
                return
            if cur_sum > target or i == len(candidates):
                return
            slate.append(candidates[i])
            helper(i+1, cur_sum+candidates[i], slate)
            slate.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, cur_sum, slate)

        res = []
        candidates.sort()
        helper(0, 0, [])
        return res