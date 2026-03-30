class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        for dest,src in prerequisites:
            inDegree[dest] += 1
        q = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                q.append(course)
        taken = []
        while q:
            curCourse = q.popleft()
            taken.append(curCourse)
            for dest,src in prerequisites:
                if src == curCourse:
                    inDegree[dest] -= 1
                    if inDegree[dest] == 0:
                        q.append(dest)
        return taken if len(taken) == numCourses else []