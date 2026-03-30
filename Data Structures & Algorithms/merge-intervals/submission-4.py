class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = []
        start, end = intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        merged.append([start,end])
        return merged