class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def canShip(cap):
            curCap, d = cap, 1
            for w in weights:
                if curCap - w < 0:
                    d += 1
                    if d > days:
                        return False
                    curCap = cap
                curCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res