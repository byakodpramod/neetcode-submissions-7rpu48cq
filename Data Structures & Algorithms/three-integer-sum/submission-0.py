class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for x in range(len(nums)-2):
            if x>0 and nums[x-1] == nums[x]:
                continue
            l,r=x+1,len(nums)-1
            while l<r:
                total = nums[x]+nums[l]+nums[r]
                if total > 0:
                    r-=1
                    continue
                elif total < 0:
                    l+=1
                    continue
                else:
                    res.append([nums[x],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r -=1
                    l += 1
                    r -= 1
        return res