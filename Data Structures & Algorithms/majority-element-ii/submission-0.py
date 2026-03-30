class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        nby3 = len(nums) // 3
        res = []
        # print(nby3,freq)
        for item in freq:
            if freq[item] > nby3:
                res.append(item)
        return res