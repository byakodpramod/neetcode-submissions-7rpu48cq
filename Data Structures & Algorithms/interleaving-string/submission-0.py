class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(i,j,k):
            if k == len(s3):
                return i==len(s1) and j==len(s2)
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            if i<len(s1) and s1[i]==s3[k] and helper(i+1,j,k+1):
                res = True
            if j<len(s2) and s2[j]==s3[k] and helper(i,j+1,k+1):
                res = True
            dp[(i,j)] = res
            return res
        dp = {}
        if len(s1)+len(s2) != len(s3):
            return False
        return helper(0,0,0)