class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        q.append((src,0,0))
        graph = defaultdict(list)
        minCost = float("inf")
        for src,des,cost in flights:
            graph[src].append((des,cost))
        while q:
            curNode,hops,cost=q.popleft()
            if curNode == dst:
                minCost = min(minCost, cost)
                continue
            if hops > k or cost > minCost:
                continue
            # if curNode in graph:
            for neigh,neighCost in graph[curNode]:
                q.append((neigh,hops+1,cost+neighCost))
        return -1 if minCost == float('inf') else minCost