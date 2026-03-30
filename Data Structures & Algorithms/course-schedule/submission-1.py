class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree=[0]*numCourses
        adj = [[] for i in range(numCourses)]
        for src,dest in prerequisites:
            inDegree[dest] += 1
            adj[src].append(dest)
        q = deque()
        for n in range(numCourses):
            if inDegree[n] == 0:
                q.append(n)
        taken = 0
        while q:
            cur = q.popleft()
            taken += 1
            for nei in adj[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return taken == numCourses