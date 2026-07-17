class TimeMap:

    def __init__(self):
        self.root = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.root[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.root:
            return ""
        items = self.root[key]
        l, r, res = 0, len(items)-1, ""
        while l<=r:
            mid = l+(r-l)//2
            if items[mid][1] <= timestamp:
                res = items[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res