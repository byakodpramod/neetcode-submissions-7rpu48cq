class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self,node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,n1,n2):
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = self.parent[p1]
        else:
            self.rank[p2] += self.rank[p2]
            self.parent[p1] = self.parent[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        eToIdx, emailGroups, n = {}, defaultdict(list), len(accounts)
        uf = UnionFind(n)
        for i,item in enumerate(accounts):
            for e in item[1:]:
                if e not in eToIdx:
                    eToIdx[e] = i
                else:
                    uf.union(i, eToIdx[e])
        for e,idx in eToIdx.items():
            leader = uf.find(idx)
            emailGroups[leader].append(e)
        result = []
        for idx,emails in emailGroups.items():
            item = [accounts[idx][0]]
            for e in sorted(emails):
                item.append(e)
            result.append(item)
        return result