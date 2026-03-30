class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        for dst,src in prerequisites:
            graph[src].append(dst)
            inDegree[dst] += 1
        q = deque()
        for n in range(numCourses):
            if inDegree[n] == 0:
                q.append(n)
        taken = 0
        while q:
            cur = q.popleft()
            taken += 1
            for nei in graph[cur]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return taken == numCourses