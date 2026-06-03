class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        time, q, freq = 0, deque(), defaultdict(int)
        for task in tasks:
            freq[task] += 1
        heap = []
        for f in freq.values():
            heapq.heappush(heap, -f)
        while heap or q:
            time += 1
            if heap:
                cur = -heapq.heappop(heap)
                cur -= 1
                if cur:
                    q.append((cur, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, -q.popleft()[0])
        return time