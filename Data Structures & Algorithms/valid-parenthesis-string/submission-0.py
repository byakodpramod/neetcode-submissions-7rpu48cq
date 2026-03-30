class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft,maxLeft=0,0
        for i in range(len(s)):
            if s[i] == "(":
                minLeft,maxLeft=1+minLeft,1+maxLeft
            elif s[i] == ")":
                minLeft,maxLeft=minLeft-1,maxLeft-1
            else:
                minLeft,maxLeft=minLeft-1,maxLeft+1
            if maxLeft < 0:
                return False
            minLeft = max(minLeft, 0)
        return minLeft == 0