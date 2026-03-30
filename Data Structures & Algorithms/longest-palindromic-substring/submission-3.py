class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        if not s:
            return ""
        if len(s) == 1:
            return s
        res = ""
        for i in range(len(s)-1):
            odd = getPalindrome(i,i)
            even = getPalindrome(i, i+1)
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res