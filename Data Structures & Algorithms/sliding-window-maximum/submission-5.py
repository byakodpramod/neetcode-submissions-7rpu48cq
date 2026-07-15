class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        q, res, left = deque(), [], 0
        for right in range(len(nums)):
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)
            if left > q[0]:
                q.popleft()
            if right >= k-1:
                res.append(nums[q[0]])
                left += 1
        return res