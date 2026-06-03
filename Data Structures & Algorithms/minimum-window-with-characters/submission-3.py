class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        tMap, window, l, resLen, res = defaultdict(int), defaultdict(int), 0, float("inf"), [-1,-1]
        for ch in t:
            tMap[ch] += 1
        have, need = 0, len(tMap)
        for r in range(len(s)):
            rChar = s[r]
            window[rChar] += 1
            if rChar in tMap and tMap[rChar] == window[rChar]:
                have += 1
            while have == need:
                lChar = s[l]
                window[lChar] -= 1
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                if lChar in tMap and window[lChar] < tMap[lChar]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""