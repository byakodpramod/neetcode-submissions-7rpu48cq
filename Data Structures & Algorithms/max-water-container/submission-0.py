class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l,r=0,len(heights)-1
        res = float("-inf")
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            res = max(res,area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res
