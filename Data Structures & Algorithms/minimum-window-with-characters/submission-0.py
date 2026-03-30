class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT, window = {}, {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("inf")
        left = 0
        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                window[s[left]] -= 1
                if s[left] in countT and countT[s[left]] > window[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""