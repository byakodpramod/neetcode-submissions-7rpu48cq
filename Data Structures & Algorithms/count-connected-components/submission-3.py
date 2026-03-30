class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
        if not edges:
            return n
        components = 0
        graph = defaultdict(list)
        visited = set()
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)
        for node in graph.keys():
            if node not in visited:
                dfs(node)
                components += 1
        return components