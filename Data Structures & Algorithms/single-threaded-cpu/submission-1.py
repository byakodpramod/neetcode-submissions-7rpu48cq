class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return []
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        time, i, heap, res = tasks[0][0], 0, [], []
        while i<len(tasks) or heap:
            while i<len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if not heap:
                time = tasks[i][0]
            if heap:
                procT, procIdx = heapq.heappop(heap)
                time += procT
                res.append(procIdx)
        return res