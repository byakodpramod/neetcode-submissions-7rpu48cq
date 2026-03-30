class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        i,j = 0,0
        while i<len(strs[0]) and j<len(strs[-1]) and strs[0][i] == strs[-1][j]:
            i += 1
            j += 1
        return strs[0][:i] if i == j else "" 