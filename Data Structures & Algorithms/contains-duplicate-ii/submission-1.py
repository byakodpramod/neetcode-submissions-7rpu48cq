class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        seen = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i-seen[nums[i]] <= k):
                    return True
            seen[nums[i]] = i
        return False