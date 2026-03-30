class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src,dst in prerequisites:
            inDegree[dst] += 1
            adj[src].append(dst)
        q = deque()
        res = []
        for n in range(numCourses):
            if inDegree[n] == 0:
                q.append(n)
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in adj[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return []
        return res[::-1]