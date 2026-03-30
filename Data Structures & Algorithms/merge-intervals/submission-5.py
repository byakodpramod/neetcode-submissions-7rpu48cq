class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                merged.append([start, end])
                start, end = intervals[i]
        merged.append([start,end])
        return merged
