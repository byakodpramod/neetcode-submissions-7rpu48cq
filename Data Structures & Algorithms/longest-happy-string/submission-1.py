class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap, res = [], ""
        for cnt,ch in [(-a,"a"), (-b,"b"), (-c,"c")]:
            if -cnt > 0:
                heapq.heappush(maxHeap, (cnt,ch))
        while maxHeap:
            curCnt, curCh = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == curCh:
                if not maxHeap:
                    break
                secCnt, secCh = heapq.heappop(maxHeap)
                res += secCh
                secCnt += 1
                if secCnt:
                    heapq.heappush(maxHeap, (secCnt, secCh))
                heapq.heappush(maxHeap, (curCnt, curCh))
            else:
                res += curCh
                curCnt += 1
                if curCnt:
                    heapq.heappush(maxHeap, (curCnt, curCh))
        return res
