class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': set(['a', 'b', 'c']),
                 '3': set(['d', 'e', 'f']),
                 '4': set(['g', 'h', 'i']),
                 '5': set(['j', 'k', 'l']),
                 '6': set(['m', 'n', 'o']),
                 '7': set(['p', 'q', 'r', 's']),
                 '8': set(['t', 'u', 'v']),
                 '9': set(['w', 'x', 'y', 'z'])}
        def helper(i,slate):
            if i == len(digits):
                res.append("".join(slate))
                return
            for ch in phone[digits[i]]:
                slate.append(ch)
                helper(i+1, slate)
                slate.pop()
        if not digits:
            return []
        res = []
        helper(0,[])
        return res