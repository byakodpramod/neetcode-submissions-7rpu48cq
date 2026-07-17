class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        q, time, freq = deque(), 0, defaultdict(int)
        for t in tasks:
            freq[t] += 1
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)
        # print(freq)
        while heap or q:
            time += 1
            if heap:
                curF = -heapq.heappop(heap)
                curF -= 1
                if curF:
                    q.append((curF, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, -q.popleft()[0])
        return time