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
        def helper(curStr, remainingStr):
            if not remainingStr:
                result.append(curStr)
                return
            for ch in phone[remainingStr[0]]:
                helper(curStr+ch, remainingStr[1:])
        result = []
        if not digits:
            return result
        else:
            helper("", digits)
            return result