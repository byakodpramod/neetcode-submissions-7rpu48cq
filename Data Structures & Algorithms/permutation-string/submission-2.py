class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map, s2Map = defaultdict(int), defaultdict(int)
        matched, l = 0, 0
        for i in range(len(s1)):
            s1Map[s1[i]] += 1
            s2Map[s2[i]] += 1
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if s1Map[ch] == s2Map[ch]:
                matched += 1
        for r in range(len(s1),len(s2)):
            if matched == 26:
                return True
            rightC = s2[r]
            s2Map[rightC] += 1
            if s2Map[rightC] == s1Map[rightC]:
                matched += 1
            elif s1Map[rightC] + 1 == s2Map[rightC]:
                matched -= 1
            leftC = s2[l]
            s2Map[leftC] -= 1
            l += 1
            if s2Map[leftC] == s1Map[leftC]:
                matched += 1
            elif s1Map[leftC] - 1 == s2Map[leftC]:
                matched -= 1
        return matched == 26