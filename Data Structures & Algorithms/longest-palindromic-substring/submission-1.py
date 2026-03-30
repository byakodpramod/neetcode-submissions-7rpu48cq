class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            # print(s[l+1:r])
            return s[l+1:r]
        
        if not s:
            return ""
        if len(s) == 1:
            return s
        result = ""
        for i in range(len(s)-1):
            odd = getPalindrome(s,i,i)
            even = getPalindrome(s,i,i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result