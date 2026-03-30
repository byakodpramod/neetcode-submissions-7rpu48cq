class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2=len(word1),len(word2)
        dp = {}
        def dfs(i,j):
            if i == len1:
                return len2-j
            elif j == len2:
                return len1-i
            elif (i,j) in dp:
                return dp[(i,j)]
            elif word1[i] == word2[j]:
                return dfs(i+1,j+1)
            else:
                res = 0
                res = min(dfs(i+1,j), dfs(i,j+1), dfs(i+1,j+1))
                dp[(i,j)] = res + 1
                return res + 1
        return dfs(0,0)