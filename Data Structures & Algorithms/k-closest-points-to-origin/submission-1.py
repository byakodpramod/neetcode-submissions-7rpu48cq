class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        q = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            if len(q) < k:
                heapq.heappush(q, (-dist,[x,y]))
            else:
                heapq.heappushpop(q, (-dist,[x,y]))
        res = []
        while q:
            res.append(heapq.heappop(q)[1])
        return res