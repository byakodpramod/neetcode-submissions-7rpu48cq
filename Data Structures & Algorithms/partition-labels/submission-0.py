class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        position = {}
        start = 0
        maxPos = 0
        output = []
        for i in range(len(s)):
            position[s[i]] = i
        for j in range(len(s)):
            maxPos = max(maxPos, position[s[j]])
            if maxPos == j:
                output.append(j-start+1)
                start = j+1
        return output