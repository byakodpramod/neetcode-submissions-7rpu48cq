class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        store = {0:1}
        curSum, res = 0, 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum not in store:
                store[curSum] = 0
            if (curSum - k) in store:
                # print(curSum, i)
                res += store[curSum-k]
            store[curSum] += 1
        # print(store)
        return res