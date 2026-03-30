class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        res, left , freq = 0, 0, {}
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            while (right-left+1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res