class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        heap = []
        q = deque()
        time = 0
        for f in freq.values():
            heapq.heappush(heap, -f)
        while heap or q:
            time += 1
            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                if count:
                    q.append((count, time+n))
            if q and q[0][1] == time:
                heapq.heappush(heap, -q.popleft()[0])
        return time