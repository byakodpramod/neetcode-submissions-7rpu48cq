class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s,l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def helper(i, slate):
            if i>=len(s):
                res.append(slate[:])
                return
            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    slate.append(s[i:j+1])
                    helper(j+1,slate)
                    slate.pop()
        
        res=[]
        helper(0,[])
        return res
        
        # res = []
        # helper(0,[])
        # return res
