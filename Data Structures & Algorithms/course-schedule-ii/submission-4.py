class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
            inDegree[dst] += 1
        q = deque()
        res = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            curNode = q.popleft()
            res.append(curNode)
            for nei in adj[curNode]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return []
        return res[::-1]