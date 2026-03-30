class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freqMap = {}
        for h in hand:
            freqMap[h] = 1 + freqMap.get(h,0)
        heap = list(freqMap.keys())
        heapq.heapify(heap)
        while heap:
            curMin = heap[0]
            # print(curMin, freqMap, heap)
            for num in range(curMin, curMin+groupSize):
                if num not in freqMap:
                    return False
                freqMap[num] -= 1
                # print(num, freqMap[num])
                if freqMap[num] == 0:
                    heapq.heappop(heap)
                    del freqMap[num]
        return len(heap) == 0
