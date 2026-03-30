class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        strsMap = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in strsMap:
                strsMap[sortedS] = []
            strsMap[sortedS].append(s)

        return strsMap.values()