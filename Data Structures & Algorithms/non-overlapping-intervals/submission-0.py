class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        prevEnd = intervals[0][1]
        result = 0
        for start, end in intervals[1:]:
            if prevEnd <= start:
                prevEnd = end
            else:
                result += 1
                prevEnd = min(prevEnd, end)
        return result