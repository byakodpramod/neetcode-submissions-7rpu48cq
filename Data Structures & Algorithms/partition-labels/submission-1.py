class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        res = []
        charToIdx = defaultdict(int)
        for i,c in enumerate(s):
            charToIdx[c] = i
        # print(charToIdx)
        max_idx = 0
        start = 0
        for i in range(len(s)):
            max_idx = max(max_idx, charToIdx[s[i]])
            if i == max_idx:
                res.append(i-start+1)
                start = i+1
        return res