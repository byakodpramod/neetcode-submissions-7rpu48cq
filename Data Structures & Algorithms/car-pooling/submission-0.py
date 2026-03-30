class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        order = []
        for cnt,src,dst in trips:
            order.append((src, cnt))
            order.append((dst, -cnt))
        order.sort(key = lambda x:x[0])
        cur = 0
        for place,ppl in order:
            cur += ppl
            if cur > capacity:
                return False
        return True