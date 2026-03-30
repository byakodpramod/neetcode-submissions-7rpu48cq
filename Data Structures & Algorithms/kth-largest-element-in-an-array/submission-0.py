class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        heap=[]
        for item in nums:
            if len(heap) < k:
                heapq.heappush(heap,item)
            else:
                heapq.heappushpop(heap,item)
        return heap[0]