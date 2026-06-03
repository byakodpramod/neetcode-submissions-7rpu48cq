class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        store = []
        for cap,src,dst in trips:
            store.append((src,cap))
            store.append((dst,-cap))
        store.sort(key= lambda x:x[0])
        curCap = 0
        for pos,cap in store:
            curCap += cap
            if curCap > capacity:
                return False
        return True