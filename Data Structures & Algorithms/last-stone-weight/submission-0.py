class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            first,second=-heapq.heappop(heap),-heapq.heappop(heap)
            if first > second:
                heapq.heappush(heap,-(first-second))
        return -heap[0] if len(heap) else 0