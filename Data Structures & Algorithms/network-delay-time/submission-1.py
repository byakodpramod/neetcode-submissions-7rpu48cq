import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times or n==0:
            return -1
        minHeap = [(0,k)]
        graph = defaultdict(list)
        for src,dest,cost in times:
            graph[src].append((dest,cost))
        visited = set()
        resTime = 0
        while minHeap:
            nodeDist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            resTime = nodeDist
            for neigh, neighDist in graph[node]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (nodeDist+neighDist, neigh))
        return resTime if len(visited) == n else -1