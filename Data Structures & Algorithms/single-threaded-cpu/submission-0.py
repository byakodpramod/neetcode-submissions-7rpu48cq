class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda x:x[0])
        heap, res = [], []
        i , time = 0, tasks[0][0]
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                procT, idx = heapq.heappop(heap)
                time += procT
                res.append(idx)
        return res