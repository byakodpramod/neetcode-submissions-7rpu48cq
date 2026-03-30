class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        l,tMap, window, res, resLen = 0, defaultdict(int), defaultdict(int), [-1,-1], float("inf")
        for c in t:
            tMap[c] += 1
        have, need = 0, len(tMap)
        for r in range(len(s)):
            rChar = s[r]
            window[rChar] += 1
            if rChar in tMap and tMap[rChar] == window[rChar]:
                have += 1
            while have == need:
                lChar = s[l]
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[lChar] -= 1
                if lChar in tMap and tMap[lChar] > window[lChar]:
                    have -= 1
                l += 1
        l,r=res
        return s[l:r+1] if res != float("inf") else ""