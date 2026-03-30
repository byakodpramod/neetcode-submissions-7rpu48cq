class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        maxH = []
        for ch in freq.keys():
            heapq.heappush(maxH, (-freq[ch], ch))
        prevCh, prevFreq = "", 0
        res = ""
        while maxH:
            curFreq, curCh = heapq.heappop(maxH)
            if prevCh and -prevFreq > 0:
                heapq.heappush(maxH,(prevFreq, prevCh))
            res += curCh
            curFreq += 1
            prevCh = curCh
            prevFreq = curFreq
        return res if len(res) == len(s) else ""