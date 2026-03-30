class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        heap = []
        freq = {}
        for n in nums:
            freq[n] = 1+freq.get(n,0)
        for num,cnt in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt,num))
            else:
                if heap[0][0] < cnt:
                    heapq.heappushpop(heap, (cnt,num))
        # print(heap)
        output = []
        for i in range(len(heap)):
            output.append(heapq.heappop(heap)[1])
        return output