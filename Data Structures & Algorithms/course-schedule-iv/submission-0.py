class Solution:
    def dfs(self, node, d, graph, visited):
        if node == d:
            return True
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if self.dfs(nei, d, graph, visited):
                    return True
        return False
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not numCourses:
            return []
        graph = defaultdict(list)
        for src,dst in prerequisites:
            graph[src].append(dst)
        res = []
        for s,d in queries:
            visited = set()
            res.append(self.dfs(s,d,graph,visited))
        return res
