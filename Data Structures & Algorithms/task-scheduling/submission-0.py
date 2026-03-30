from collections import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()
        time = 0
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)
        for count in freq.values():
            heapq.heappush(heap, -count)
        while heap or q:
            time += 1
            if heap:
                count = -1 * heapq.heappop(heap)
                count -= 1
                if count:
                    q.append((count, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, -q.popleft()[0])
        return time