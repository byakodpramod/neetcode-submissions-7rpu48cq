class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        l,r = 1,max(piles)
        while l<r:
            mid = l + (r-l)//2
            midRate = 0
            for p in piles:
                midRate += math.ceil(float(p/mid))
            if midRate <= h:
                r = mid
            else:
                l = mid+1
        return r