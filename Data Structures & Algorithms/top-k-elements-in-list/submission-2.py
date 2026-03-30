import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        heap = []
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
        for num,cnt in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt,num))
            else:
                if cnt > heap[0][0]:
                    heapq.heappushpop(heap, (cnt,num))
        output = []
        for i in range(len(heap)):
            output.append(heapq.heappop(heap)[1])
        return output