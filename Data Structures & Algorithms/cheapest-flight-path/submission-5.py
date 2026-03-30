class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        q = deque()
        q.append((0,src,0))
        minCost = float('inf')
        for sr,dt,cost in flights:
            graph[sr].append((dt,cost))
        while q:
            curCost,curNode,stops = q.popleft()
            # print(curCost, curNode, stops)
            if curNode == dst:
                minCost = min(minCost, curCost)
                continue
            if stops > k or curCost > minCost:
                continue
            for nei,neiCost in graph[curNode]:
                q.append((curCost+neiCost, nei, stops+1))
        return -1 if minCost == float('inf') else minCost