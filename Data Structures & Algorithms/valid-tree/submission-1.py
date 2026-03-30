class Solution:
    def isCycle(self,graph,visited,parent,node):
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                parent[neigh] = node
                self.isCycle(graph,visited,parent,neigh)
            else:
                if node in parent and parent[node] == neigh:
                    continue
                else:
                    return True
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
                isCycle = self.isCycle(graph,visited,parent,node)
                if isCycle:
                    return False
        return components == 1