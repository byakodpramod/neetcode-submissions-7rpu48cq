class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return 0
        graph = defaultdict(list)
        for src,dst,t in times:
            graph[src].append((dst,t))
        heap = []
        heap.append((0,k))
        res = 0
        visited = set()
        while heap:
            curT, curNode = heapq.heappop(heap)
            # print(curNode, curT)
            if curNode in visited:
                continue
            visited.add(curNode)
            res = curT
            for nei,neiT in graph[curNode]:
                if nei not in visited:
                    heapq.heappush(heap, (curT+neiT, nei))
        return res if len(visited) == n else -1