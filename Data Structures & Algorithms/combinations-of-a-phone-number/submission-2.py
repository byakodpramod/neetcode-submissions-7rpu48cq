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
        def helper(slate, i):
            if i >= len(digits):
                res.append(slate)
                return
            for letter in phone[digits[i]]:
                slate += letter
                helper(slate, i+1)
                slate = slate[:-1]
        res = []
        if not digits:
            return []
        else:
            helper("", 0)
            return res