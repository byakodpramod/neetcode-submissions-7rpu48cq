class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l,r,s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def helper(i, slate):
            if i >= len(s):
                res.append(slate[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(i,j,s):
                    slate.append(s[i:j+1])
                    helper(j+1, slate)
                    slate.pop()
            return res
        res = []
        helper(0, [])
        return res             