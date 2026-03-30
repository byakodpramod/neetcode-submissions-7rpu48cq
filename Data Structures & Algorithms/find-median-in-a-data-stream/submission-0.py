from heapq import *
class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if len(self.leftMaxHeap) == len(self.rightMinHeap):
            heappush(self.rightMinHeap, -heappushpop(self.leftMaxHeap, -num))
        else:
            heappush(self.leftMaxHeap, -heappushpop(self.rightMinHeap, num))

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) == len(self.rightMinHeap):
            return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2.0
        else:
            return self.rightMinHeap[0]
        