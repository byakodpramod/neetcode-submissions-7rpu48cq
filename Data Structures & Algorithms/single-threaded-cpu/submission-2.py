class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return tasks
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x:x[0])
        heap, i, time, res = [], 0, tasks[0][0], []
        while i<len(tasks) or heap:
            while i<len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                endT, idx = heapq.heappop(heap)
                res.append(idx)
                time += endT
        return res