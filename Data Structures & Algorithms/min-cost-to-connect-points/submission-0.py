class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x,y=points[i]
            for j in range(i+1,N):
                x1,y1=points[j]
                dist = abs(x1-x) + abs(y1-y)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        visit = set()
        minH = [[0,0]]
        res = 0
        while len(visit) < N:
            curCost, p = heapq.heappop(minH)
            if p in visit:
                continue
            visit.add(p)
            res += curCost
            for neiCost,nei in adj[p]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res