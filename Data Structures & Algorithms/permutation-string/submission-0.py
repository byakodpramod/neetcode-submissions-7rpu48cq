class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Map,s2Map={},{}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s1Map[c] = 0
            s2Map[c] = 0
        for i in range(len(s1)):
            s1Map[s1[i]] += 1
            s2Map[s2[i]] += 1
        matches=0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s1Map[c] == s2Map[c]:
                matches += 1
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            rChar = s2[r]
            s2Map[rChar] += 1
            if s1Map[rChar] == s2Map[rChar]:
                matches+=1
            elif s1Map[rChar] + 1 == s2Map[rChar]:
                matches-=1
            lChar = s2[l]
            s2Map[lChar] -= 1
            if s1Map[lChar] == s2Map[lChar]:
                matches+=1
            elif s1Map[lChar] - 1 == s2Map[lChar]:
                matches-=1
            l+=1
        return matches == 26