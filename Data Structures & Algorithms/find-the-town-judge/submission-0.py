class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1
        inDegree = {i:0 for i in range(1,n+1)}
        outDegree = {i:0 for i in range(1,n+1)}
        for src,dst in trust:
            inDegree[dst] += 1
            outDegree[src] += 1
        for p in range(1,n+1):
            if inDegree[p] == n-1 and outDegree[p] == 0:
                return p
        return -1