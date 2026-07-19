class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        q = []
        heapq.heappush(q,(0,src,0))
        visited = set()
        res = float("inf")
        for s,d,cost in flights:
            graph[s].append((d,cost))
        while q:
            dist, cur, stops = heapq.heappop(q)
            if cur == dst:
                res = min(res, dist)
            if cur in visited:
                continue
            if stops > k or dist > res:
                continue
            for nei, ncost in graph[cur]:
                heapq.heappush(q,(dist+ncost, nei, stops+1))
        return -1 if res == float('inf') else res