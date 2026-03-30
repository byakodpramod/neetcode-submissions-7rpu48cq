class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times or n == 0:
            return -1
        graph = defaultdict(list)
        for src,dst,t in times:
            graph[src].append((dst,t))
        visited = set()
        q = [(0,k)]
        resT = 0
        while q:
            curT,curNode = heapq.heappop(q)
            if curNode in visited:
                continue
            visited.add(curNode)
            resT = curT
            for nei,t in graph[curNode]:
                if nei not in visited:
                    heapq.heappush(q, (curT+t, nei))
        return resT if len(visited) == n else -1