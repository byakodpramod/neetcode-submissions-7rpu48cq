class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        s2Map = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        matched = 0
        for i in range(len(s1)):
            s1Map[s1[i]] += 1
            s2Map[s2[i]] += 1
        for c in "abcdefghijklmnopqrstuvwxyz":
            if s1Map[c] == s2Map[c]:
                matched+=1
        l = 0
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
            if s1Map[leftC] == s2Map[leftC]:
                matched += 1
            elif s1Map[leftC] - 1 == s2Map[leftC]:
                matched -= 1
        return matched == 26