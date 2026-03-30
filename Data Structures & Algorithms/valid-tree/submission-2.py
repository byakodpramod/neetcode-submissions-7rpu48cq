class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def isCycle(cur):
            visited.add(cur)
            for nei in graph[cur]:
                if nei not in visited:
                    parent[nei] = cur
                    isCycle(nei)
                else:
                    if cur in parent and parent[cur] == nei:
                        continue
                    else:
                        return True
            return False
        if not edges:
            return True
        graph = defaultdict(list)
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)
        visited = set()
        parent = {}
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                cycle = isCycle(node)
                if cycle:
                    return False
        return components == 1