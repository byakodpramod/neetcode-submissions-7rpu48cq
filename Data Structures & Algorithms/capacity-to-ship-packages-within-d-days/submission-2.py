class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(mid):
            curW, d = 0, 1
            for w in weights:
                if curW + w > mid:
                    curW = w
                    d += 1
                    if d > days:
                        return False
                else:
                    curW += w
            return True
        if not weights:
            return 0
        l,r = max(weights),sum(weights)
        while l<r:
            mid = l+(r-l)//2
            if canShip(mid):
                res = r
                r = mid
            else:
                l = mid+1
        return l