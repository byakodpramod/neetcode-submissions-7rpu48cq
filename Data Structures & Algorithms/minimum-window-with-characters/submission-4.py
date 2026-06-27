class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t is None:
            return ""
        tMap, window = defaultdict(int), defaultdict(int)
        for c in t:
            tMap[c] += 1
        have, need, l, res, resLen = 0, len(tMap), 0, [-1,-1], float("inf")
        for r in range(len(s)):
            rChar = s[r]
            window[rChar] += 1
            if rChar in tMap and tMap[rChar] == window[rChar]:
                have += 1
            while have == need:
                lChar = s[l]
                window[lChar] -= 1
                if resLen > (r-l+1):
                    resLen = min(resLen, r-l+1)
                    res = [l,r]
                if lChar in tMap and tMap[lChar] > window[lChar]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""