class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return nums
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        q = []
        for n in freq.keys():
            if len(q) < k:
                heapq.heappush(q, [freq[n], n])
            else:
                if freq[n] > q[0][0]:
                    heapq.heappushpop(q, [freq[n], n])
        return [n[1] for n in q]