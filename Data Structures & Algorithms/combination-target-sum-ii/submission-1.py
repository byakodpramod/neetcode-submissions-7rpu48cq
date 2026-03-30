class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, cur_sum, slate):
            if cur_sum == target:
                result.append(slate[:])
                return
            for i in range(len(arr)):
                if cur_sum+arr[i] > target:
                    break
                if i>0 and arr[i] == arr[i-1]:
                    continue
                slate.append(arr[i])
                helper(arr[i+1:], cur_sum+arr[i], slate)
                slate.pop()
        candidates.sort()
        result = []
        helper(candidates, 0, [])
        return result