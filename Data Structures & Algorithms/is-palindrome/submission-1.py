class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        i,j=0,len(s)-1
        while i<=j:
            # print(i,j)
            if not self.alphaNum(s[i]):
                i+=1
                continue
            if not self.alphaNum(s[j]):
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                # print(s[i],s[j])
                return False
            i+=1
            j-=1
        return True