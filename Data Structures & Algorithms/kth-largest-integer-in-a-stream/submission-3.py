class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            heapq.heappush(self.q, val)
        else:
            heapq.heappushpop(self.q, val)
        return self.q[0]
