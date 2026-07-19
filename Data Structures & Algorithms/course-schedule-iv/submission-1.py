class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(node,dst,visited):
            if node == dst:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei,dst,visited):
                        return True
            return False

        if not numCourses:
            return []
        graph, result = defaultdict(list), []
        for d,s in prerequisites:
            graph[s].append(d)
        for d,s in queries:
            visited = set()
            result.append(dfs(s,d,visited))
        return result