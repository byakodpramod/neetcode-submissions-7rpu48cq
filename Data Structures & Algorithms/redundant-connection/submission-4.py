class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        n = len(edges)
        graph = defaultdict(list)
        inDegree = {i:0 for i in range(1,n+1)}
        q = deque()
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            inDegree[a] += 1
            inDegree[b] += 1
        # print(inDegree)
        for node in range(1, n+1):
            if inDegree[node] == 1:
                q.append(node)
        while q:
            cur = q.popleft()
            inDegree[cur] -= 1
            for nei in graph[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 1:
                    q.append(nei)
        print(inDegree)
        for a,b in reversed(edges):
            if inDegree[a] == 2 and inDegree[b] > 0:
                return [a,b]
        return []