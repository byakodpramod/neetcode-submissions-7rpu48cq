class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r,res=0,len(people)-1,0
        while l<=r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if people[l] <= remain:
                l += 1
        return res