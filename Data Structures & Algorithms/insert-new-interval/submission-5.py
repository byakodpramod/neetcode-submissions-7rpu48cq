class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        print(intervals)
        intervals.sort()
        result = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start, end = intervals[i]
        result.append([start,end])
        return result