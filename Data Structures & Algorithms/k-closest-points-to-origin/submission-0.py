import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        res=[]
        heap=[]
        for point in points:
            dist=math.sqrt(point[0]**2 + point[1]**2)
            if len(heap) < k:
                heapq.heappush(heap, (-dist,point))
            else:
                heapq.heappushpop(heap, (-dist,point))
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res