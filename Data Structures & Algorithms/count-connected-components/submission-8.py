class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        components, graph, visited = 0, defaultdict(list), set()
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        return components