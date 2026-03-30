class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(i, slate):
            if i == len(s):
                res.append(" ".join(slate))
                return
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    slate.append(s[i:j+1])
                    helper(j+1, slate)
                    slate.pop()
        res = []
        wordDict = set(wordDict)
        helper(0,[])
        return res