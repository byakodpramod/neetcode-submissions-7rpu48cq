class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabetList = [0] * 26
        for i in range(len(s)):
            alphabetList[ord(s[i]) - ord('a')] += 1
            alphabetList[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if alphabetList[i] != 0:
                return False
        return True