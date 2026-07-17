class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        people.sort()
        l,r,result = 0,len(people)-1,0
        while l<=r:
            if people[l]+people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            result += 1
        return result