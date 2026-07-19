class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        if not edges:
            return []
        parent = [n for n in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]
        for u,v in edges:
            if not union(u,v):
                return [u,v]