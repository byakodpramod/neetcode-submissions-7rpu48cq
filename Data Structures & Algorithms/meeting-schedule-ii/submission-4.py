"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res, cur = 0, 0
        store = []
        for i in range(len(intervals)):
            s,e = intervals[i].start, intervals[i].end
            store.append((s,1))
            store.append((e,-1))
        for item in sorted(store):
            cur += item[1]
            res = max(res, cur)
        return res