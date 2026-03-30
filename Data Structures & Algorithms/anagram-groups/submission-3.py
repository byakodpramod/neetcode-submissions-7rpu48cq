class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        strsMap = {}
        for s in strs:
            alphaList = [0]*26
            for i in range(len(s)):
                alphaList[ord(s[i]) - ord('a')] += 1
            alphaTuple = tuple(alphaList)
            if tuple(alphaTuple) not in strsMap:
                strsMap[alphaTuple] = []
            strsMap[alphaTuple].append(s)

        return strsMap.values()