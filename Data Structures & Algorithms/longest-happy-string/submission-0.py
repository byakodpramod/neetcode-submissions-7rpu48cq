class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap, res = [], ""
        for c,ch in [(-a,"a"), (-b,"b"), (-c,"c")]:
            if -c > 0:
                heapq.heappush(maxHeap,(c,ch))
        while maxHeap:
            curCnt, curCh = heapq.heappop(maxHeap)
            if len(res) > 1 and curCh == res[-1] == res[-2]:
                if not maxHeap:
                    break
                cnt2, ch2 = heapq.heappop(maxHeap)
                res += ch2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(maxHeap, (cnt2, ch2))
                heapq.heappush(maxHeap, (curCnt, curCh))
            else:
                res += curCh
                curCnt += 1
                if curCnt:
                    heapq.heappush(maxHeap, (curCnt, curCh))
        return res