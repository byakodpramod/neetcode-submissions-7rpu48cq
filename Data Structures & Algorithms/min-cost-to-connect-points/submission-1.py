class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        N = len(points)
        graph = defaultdict(list)
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        visited = set()
        q = [[0,0]]
        res = 0
        while len(visited) < N:
            curDist, curP = heapq.heappop(q)
            if curP in visited:
                continue
            visited.add(curP)
            res += curDist
            for neiDist, nei in graph[curP]:
                if nei not in visited:
                    heapq.heappush(q, [neiDist, nei])
        return res