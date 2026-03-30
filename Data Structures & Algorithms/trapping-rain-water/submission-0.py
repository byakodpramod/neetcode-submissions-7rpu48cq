class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res = 0
        if height:
            l_max,r_max=height[0],height[len(height)-1]
        else:
            return 0
        while l<=r:
            if height[l] < height[r]:
                if l_max < height[l]:
                    l_max = height[l]
                else:
                    res += l_max-height[l]
                l+=1
            else:
                if r_max < height[r]:
                    r_max = height[r]
                else:
                    res += r_max-height[r]
                r-=1
        return res