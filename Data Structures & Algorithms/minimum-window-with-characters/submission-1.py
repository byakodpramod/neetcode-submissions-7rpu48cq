# s = OUZODYXAZV
# t = XYZ
# l = 1
# r = 6
# have = 3
# need = 3
# window = {O:2, U:1, Z:1, D:1, Y:1, X:1}
# tMap = {X:1, Y=1, Z=1}
# resLen = 6
# res = [0,6]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        window, tMap, l = defaultdict(int), defaultdict(int), 0
        res, resLen = [-1,-1], float('inf')
        for ch in t:
            tMap[ch] += 1
        have, need = 0, len(tMap)
        for r in range(len(s)):
            rChar = s[r]
            window[rChar] += 1
            if rChar in tMap and tMap[rChar] == window[rChar]:
                have += 1
            # print(have, need, l, r)
            while have == need:
                # print(here)
                lChar = s[l]
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[lChar] -= 1
                if lChar in tMap and tMap[lChar] > window[lChar]:
                    have -= 1
                l += 1
        l,r = res
        # print(l,r)
        return s[l:r+1] if res != float("inf") else ""